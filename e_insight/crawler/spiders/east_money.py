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


# https://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?cb=datatable2703311&type=GJZB&sty=ZGZB&js=(%7Bdata%3A%5B(x)%5D%2Cpages%3A(pc)%7D)&p=1&ps=20&mkt=11&_=1619505235475

class EastMoney(scrapy.Spider):
    name = "east_money"
    start_urls = ["https://data.eastmoney.com/cjsj/hbgyl.html"]
    use_chrome_proxy = True

    def parse(self, response, **kwargs):
        soup = Soup(response.text)
        print(soup)
        div = soup.find("div", attrs={"class": "content"})
        print(div)
