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


class EastMoney(scrapy.Spider):
    name = "east_money"
    start_urls = ["https://data.eastmoney.com/cjsj/hbgyl.html"]
    use_chrome_proxy = True

    def parse(self, response, **kwargs):
        soup = Soup(response.text)
        div = soup.find("div", attrs={"class": "content"})
        print(div)
