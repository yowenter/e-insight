import logging
import scrapy
import time
import re
import json
from datetime import datetime
from xml.dom.minidom import parseString

from prometheus_client.metrics import Gauge

from e_insight.crawler.items import MetricItem

LOG = logging.getLogger(__name__)


class USABond(scrapy.Spider):
    name = "usa_bond"
    cur_month = datetime.now().month
    cur_year = datetime.now().year

 # https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%205%20and%20year(NEW_DATE)%20eq%202021
    url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%20{month}%20and%20year(NEW_DATE)%20eq%20{year}".format(
        month=cur_month, year=cur_year)
    start_urls = [url]

    def __init__(self, *args, **kwargs):
        super(USABond, self).__init__(*args, **kwargs)
        # self.proxy_pool = ["http://localhost:8080/fetch"]

    # def start_requests(self):
    #     cur_month = datetime.now().month
    #     cur_year = datetime.now().year
    #
    #     url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%20{month}%20and%20year(NEW_DATE)%20eq%20{year}".format(
    #         month=cur_month, year=cur_year)
    #     self.start_urls = [url]
    #     super(USABond, self).start_requests()

    def parse(self, response, **kwargs):
        tree = parseString(response.text)
        for item in ["BC_10YEAR", "BC_1YEAR", "BC_1MONTH", "BC_6MONTH", "BC_5YEAR", "BC_3YEAR"]:
            ele = tree.getElementsByTagName("entry")[-1].getElementsByTagName("content")[0]
            rate = ele.getElementsByTagName("m:properties")[0].getElementsByTagName("d:%s" % item)[0].childNodes[
                0].data

            yield MetricItem(
                name="US_BONDS",
                value=rate,
                labels={"yield": item},
                type=Gauge._type,
                description="美国国债利率"
            )


class CNBCQuotes(scrapy.Spider):
    name = "cnbc_quotes"

    start_urls = ["https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?output=json&symbols=%s" % i
                  for i in
                  ["US10Y", "US2Y", "VIX", ".IXIC", ".DJI", ".SPX", ".HSI", ".SZI", ".SSEC", "@SI.1", "@HG.1", "@CT.1",
                   "@S.1", "@W.1", "@PL.1", "@SI.1", "@CL.1", "BTC.CM="]]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        data = data.get("FormattedQuoteResult", {}).get("FormattedQuote", [])[-1]
        symbol = data.get("symbol", "")
        name = re.search(r"(\w| )+", data.get("name", "")).group().strip()
        change = data.get("change", "").replace("+", "")
        for price in ["last", "high", "low", "open"]:
            v = data[price].replace(",", "")
            if str(v).endswith("%"):
                v = v[:-1]
            yield MetricItem(
                name="CNBC_QUOTE",
                value=float(v),
                labels={"price": price, "symbol": symbol, "name": name},
                type=Gauge._type,
                description="CNBC QUOTE PRICE"
            )

        yield MetricItem(
            name="CNBC_QUOTE_CHANGE",
            value=float(change),
            labels={"symbol": symbol, "name": name},
            type=Gauge._type,
            description="CNBC QUOTES CHANGE"
        )
