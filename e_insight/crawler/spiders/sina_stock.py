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
    start_urls = ["http://hq.sinajs.cn/list=%s" % ",".join(["sh000300", "sh000001", "sh600519", "hk00700", "hk03690"])]
    data_idx = {
        "open": 1,
        "closed": 2,
        "current": 3,
        "max": 4,
        "min": 5
    }

    hk_data_idx = {

        "open": 1,
        "closed": 2,
        "current": 5,
        "max": 3,
        "min": 4
    }

    def parse(self, response, **kwargs):

        for line in response.text.split("\n"):
            if len(line.split("=")) != 2:
                print(line)
                continue
            name, data = line.split("=")
            points = data.strip().split(",")
            stock_name = points[0].replace('"', "")
            points = points[1:]
            data_idx = self.data_idx
            if not re.match("(\d|\.)+", points[0]):
                points = points[1:]
                data_idx = self.hk_data_idx

            for k, idx in data_idx.items():
                idx = idx
                stockNo = name.split(" ")[-1][7:]
                yield MetricItem(
                    name="sina_stocks",
                    value=points[idx - 1],
                    type=Gauge._type,
                    labels={
                        "stock_no": stockNo,
                        "stock_name": stock_name,
                        "price": k
                    },
                    description="新浪股市"
                )
