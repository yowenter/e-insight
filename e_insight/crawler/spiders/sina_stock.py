import logging
import scrapy
import time
from datetime import datetime
from xml.dom.minidom import parseString
import re

from prometheus_client.metrics import Gauge

from e_insight.crawler.items import MetricItem
from bs4 import BeautifulSoup as Soup

LOG = logging.getLogger(__name__)


class SinaStock(scrapy.Spider):
    name = "sina_stock"
    start_urls = ["http://hq.sinajs.cn/list=%s" % ",".join(["sh000300", "sh000001", "sh600519", "hk00700"])]
    data_idx = {
        "open": 1,
        "closed": 2,
        "current": 3,
        "max": 4,
        "min": 5
    }

    def parse(self, response, **kwargs):
        for line in response.text.split("\n"):
            if len(line.split("=")) != 2:
                print(line)
                continue
            name, data = line.split("=")
            points = data.strip().split(",")
            p = 0
            help = ""
            if not re.match("(\d|\.)+", points[0]):
                p = 1
                help = points[0].replace('"', "")

            for k, idx in self.data_idx.items():
                idx = idx + p
                metricName = name.split(" ")[-1] + "_" + k
                yield MetricItem(
                    name=metricName,
                    value=points[idx],
                    type=Gauge._type,
                    description="新浪股市 %s " % metricName + help
                )
