import logging
import scrapy
import time

LOG = logging.getLogger(__name__)


class EastMoneySpider(scrapy.Spider):
    name = "east_money_spider"
    start_urls = ["http://www.baidu.com"]

    def __init__(self, *args, **kwargs):
        super(EastMoneySpider, self).__init__(*args, **kwargs)
        # self.proxy_pool = ["http://localhost:8080/fetch"]

    def parse(self, response, **kwargs):
        time.sleep(10)
        print("done")
        pass


from scrapy.crawler import CrawlerProcess

p = CrawlerProcess()
p.crawl(EastMoneySpider)
