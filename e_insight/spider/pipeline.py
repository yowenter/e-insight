import logging
import requests
import json

from prometheus_client.core import Metric, GaugeMetricFamily

LOG = logging.getLogger(__name__)

from prometheus_client.utils import floatToGoString

MetricsMap = dict()


def sample_line(s):
    if s.labels:
        labelstr = '{{{0}}}'.format(','.join(
            ['{0}="{1}"'.format(
                k, v.replace('\\', r'\\').replace('\n', r'\n').replace('"', r'\"'))
                for k, v in sorted(s.labels.items())]))
    else:
        labelstr = ''
    timestamp = ''
    if s.timestamp is not None:
        # Convert to milliseconds.
        timestamp = ' {0:d}'.format(int(float(s.timestamp) * 1000))
    return '{0}{1} {2}{3}\n'.format(
        s.name, labelstr, floatToGoString(s.value), timestamp)


def MetricsUploader(item):
    metric = None
    k = "%s_%s" % (item["type"], item["name"])
    if MetricsMap.get(k, None) is None:
        if item["type"] == "gauge":
            metric = GaugeMetricFamily(item["name"], item["description"])
            MetricsMap[k] = metric
    else:
        metric = MetricsMap[k]
    LOG.debug("metric %s", metric)
    if metric is not None:
        metric.add_metric([], item["value"])

    return "success"


def MetricsHandler():
    output = list()
    for metric in MetricsMap.values():
        mname = metric.name
        mtype = metric.type
        # Munging from OpenMetrics into Prometheus format.
        if mtype == 'counter':
            mname = mname + '_total'
        elif mtype == 'info':
            mname = mname + '_info'
            mtype = 'gauge'
        elif mtype == 'stateset':
            mtype = 'gauge'
        elif mtype == 'gaugehistogram':
            # A gauge histogram is really a gauge,
            # but this captures the strucutre better.
            mtype = 'histogram'
        elif mtype == 'unknown':
            mtype = 'untyped'

        output.append('# HELP {0} {1}\n'.format(
            mname, metric.documentation.replace('\\', r'\\').replace('\n', r'\n')))
        output.append('# TYPE {0} {1}\n'.format(mname, mtype))
        om_samples = {}
        for s in metric.samples:
            for suffix in ['_created', '_gsum', '_gcount']:
                if s.name == metric.name + suffix:
                    # OpenMetrics specific sample, put in a gauge at the end.
                    om_samples.setdefault(suffix, []).append(sample_line(s))
                    break
            else:
                output.append(sample_line(s))
        for suffix, lines in sorted(om_samples.items()):
            output.append('# TYPE {0}{1} gauge\n'.format(metric.name, suffix))
            output.extend(lines)

    return ''.join(output).encode('utf-8')


class PrometheusMetricItemPipeline:

    def process_item(self, item, spider):
        LOG.info("process item %s from spider %s", item, spider.name)
        if item.__class__.__name__ != "MetricItem":
            LOG.info("item type %s not MetricItem. ", item.__class__.__name__)
            return
        resp = requests.post("http://localhost:8000/metrics/data", json={
            "name": item["name"],
            "type": item["type"],
            "description": item["description"],
            "value": item["value"]
        })
        LOG.info("upload metrics data, resp %s", resp.status_code)
