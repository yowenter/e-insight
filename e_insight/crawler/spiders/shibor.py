import logging
import scrapy
import time
from datetime import datetime
from xml.dom.minidom import parseString
import re
import json

from prometheus_client.metrics import Gauge

from e_insight.crawler.items import MetricItem
from bs4 import BeautifulSoup as Soup

LOG = logging.getLogger(__name__)


class ShiborShanghaiLPR(scrapy.Spider):
    name = "shanghai_shibor_lpr"
    start_urls = ["http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/bk-lpr.json"]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        data = data["records"]
        for rec in data:
            yield MetricItem(
                name="shibor_lpr",
                value=rec["shibor"],
                type=Gauge._type,
                labels={
                    "yield": rec["termCode"]
                },
                description="shibor lpr shanghai"
            )


class ShiborShanghai(scrapy.Spider):
    name = "shanghai_shibor"
    start_urls = ["http://www.shibor.org/shibor/web/html/shibor.html"]

    def parse(self, response, **kwargs):
        soup = Soup(response.text)
        table = soup.find("table", attrs={"class": "shiborquxian"})
        trs = table.find_all("tr")
        for tr in trs[:-1]:
            tds = tr.find_all("td")
            yield MetricItem(
                name="shibor",
                value=float(re.search("(\d|\.)+", tds[4].text).group()),
                type=Gauge._type,
                labels={
                    "yield": tds[1].text
                },
                description="shibor"
            )

            yield MetricItem(
                name="shibor_inc_bp",
                value=float(re.search("(\d|\.)+", tds[4].text).group()),
                labels={
                    "yield": tds[1].text
                },
                type=Gauge._type,
                description="shibor inc bp"
            )
