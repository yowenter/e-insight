import logging
import scrapy
import time
from datetime import datetime
from xml.dom.minidom import parseString

from prometheus_client.metrics import Gauge

LOG = logging.getLogger(__name__)


class USABond(scrapy.Spider):
    name = "usa_bond"
    cur_month = datetime.now().month
    cur_year = datetime.now().year

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
        for item in ["BC_10YEAR", "BC_1YEAR"]:
            ele = tree.getElementsByTagName("entry")[-1].getElementsByTagName("content")[0]
            rate = ele.getElementsByTagName("m:properties")[0].getElementsByTagName("d:%s" % item)[0].childNodes[
                0].data

            print(rate)
