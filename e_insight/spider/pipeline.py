import logging

from prometheus_client import Gauge

LOG = logging.getLogger(__name__)


class PrometheusMetricItemPipeline:
    def process_item(self, item, spider):
        LOG.info("process item %s from spider %s", item, spider.name)
        if item.__class__.__name__ != "MetricItem":
            LOG.info("item type %s not MetricItem. ", item.__class__.__name__)
            return
