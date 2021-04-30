from scrapy.crawler import CrawlerProcess
from e_insight.crawler.spiders.usa_bond import USABond
from e_insight.crawler.settings import settings

from multiprocessing import Process


def start_crawl(spider_cls):
    def f():
        p = CrawlerProcess(settings=settings)
        p.crawl(spider_cls)
        p.start()

    p = Process(target=f)
    p.start()

    # p._startedBefore = False
    # p.start(stop_after_crawl=False)
    # p._signal_kill(signal.SIGHUP, None)

    # p._signal_shutdown(signal.SIGKILL, None)
