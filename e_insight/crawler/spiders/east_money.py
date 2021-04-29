import logging
import scrapy
import json
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
    start_urls = [
        "https://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GJZB&sty=ZGZB&p=1&ps=200&mkt=11"]

    # use_chrome_proxy = True

    def parse(self, response, **kwargs):
        data = json.loads(response.text[1:-1])
        points = data[0].split(",")[1:]

        for i in range(0, 9, 3):
            yield MetricItem(
                name="money_supply",
                value=points[i],
                labels={"m": "m%d" % (2 - int(i / 3))},
                type=Gauge._type,
                description="货币供应量"
            )
            yield MetricItem(
                name="money_supply_yoy",
                value=points[i + 1],
                labels={"m": "m%d" % (2 - int(i / 3))},
                type=Gauge._type,
                description="货币供应量 yoy"
            )

            yield MetricItem(
                name="money_supply_inc",
                value=points[i + 2],
                labels={"m": "m%d" % (2 - int(i / 3))},
                type=Gauge._type,
                description="货币供应量环比"
            )


class EastMoneyTreasury(scrapy.Spider):
    name = "east_money_treasury"
    start_urls = [
        "http://datacenter.eastmoney.com/api/data/get?type=RPTA_WEB_TREASURYYIELD&sty=ALL&st=SOLAR_DATEp=1&ps=99999"]

    # use_chrome_proxy = True

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        data = data["result"]["data"][0]

        yield MetricItem(
            name="treasury_yield_ror",
            value=data["EMG00001310"],
            description="国债收益率",
            type=Gauge._type,
            labels={"yield": "10year", "country": "us"}
        )

        yield MetricItem(
            name="treasury_yield_ror",
            value=data["EMG00001306"],
            description="国债收益率",
            type=Gauge._type,
            labels={"yield": "2year", "country": "us"}
        )

        yield MetricItem(
            name="treasury_yield_ror",
            value=data["EMM00166466"],
            description="国债收益率",
            type=Gauge._type,
            labels={"yield": "10year", "country": "cn"}
        )

        yield MetricItem(
            name="treasury_yield_ror",
            value=data["EMM00588704"],
            description="国债收益率",
            type=Gauge._type,
            labels={"yield": "2year", "country": "cn"}
        )
