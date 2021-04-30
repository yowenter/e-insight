import logging
from flask import Flask
from datetime import datetime

from e_insight.crawler.pipeline import MetricsHandler, MetricsUploader

from e_insight.crawler import start_crawl

from multiprocessing import Process
import time
from filelock import FileLock

from flask import request

import schedule

LOG = logging.getLogger(__name__)

# Create my app
app = Flask(__name__)


@app.route("/metrics/crawler")
def crawler_metrics():
    return MetricsHandler()


@app.route("/metrics/data", methods=["POST"])
def upload_metrics():
    data = request.json
    return MetricsUploader(data)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


# gunicorn e_insight.app:app
# gunicorn --log-level debug  e_insight.app:app_dispatch --reload -w 1 --bind 0.0.0.0


from e_insight.crawler.spiders.usa_bond import USABond
from e_insight.crawler.spiders.east_money import EastMoney, EastMoneyTreasury, EastMoneyTradeFlow
from e_insight.crawler.spiders.sina_stock import SinaStock


def scheduler():
    print("scheduler started.")
    LOG.info("scheduler started.")
    schedule.every(30).seconds.do(ping)
    schedule.every(10).seconds.do(start_crawl, EastMoneyTreasury, EastMoneyTradeFlow)
    schedule.every(10).minutes.do(start_crawl, EastMoney)
    schedule.every(5).minutes.do(start_crawl, USABond)
    schedule.every(60).seconds.do(start_crawl, SinaStock)

    lock = FileLock("scheduler.lock", timeout=3)
    with lock:
        while True:
            schedule.run_pending()
            time.sleep(3)


def ping():
    LOG.info("scheduler ping at %s.", datetime.now())


proc = Process(target=scheduler)
proc.start()

if __name__ == '__main__':
    #    app.run(debug=True, port=5050)

    app.run(port=8000)
