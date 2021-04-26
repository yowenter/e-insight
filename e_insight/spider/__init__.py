from scrapy.crawler import CrawlerProcess
import signal
from e_insight.spider.usa_bond import USABond
from e_insight.spider.settings import settings

from multiprocessing import Process


def start_crawl():
    def f():
        p = CrawlerProcess(settings=settings)
        p.crawl(USABond)
        p.start()

    p = Process(target=f)
    p.start()

    # p._startedBefore = False
    # p.start(stop_after_crawl=False)
    # p._signal_kill(signal.SIGHUP, None)

    # p._signal_shutdown(signal.SIGKILL, None)
