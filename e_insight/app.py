import logging
from flask import Flask
from datetime import datetime
from prometheus_client import CollectorRegistry, generate_latest
from e_insight.crawler.pipeline import MetricsHandler, MetricsUploader

from e_insight.crawler import start_crawl

from multiprocessing import Process
import time
from filelock import FileLock

from flask import request

from e_insight import collector
import schedule

LOG = logging.getLogger(__name__)

# Create my app
app = Flask(__name__)

# Init Collector registry
registry = CollectorRegistry()

cn_registry = CollectorRegistry()

stocks_registry = CollectorRegistry()

# for c in collector.us_macro_collectors:
#     registry.register(c)

for c in collector.cn_macro_collectors:
    cn_registry.register(c)

for c in collector.stocks_collectors:
    stocks_registry.register(c)


@app.route("/metrics")
def metrics():
    # todo use cronjob to refresh cache
    # system = generate_latest()
    custom = generate_latest(registry=registry)
    return custom


@app.route("/metrics/cn")
def cn_metrics():
    # todo use cronjob to refresh cache
    # system = generate_latest()
    custom = generate_latest(registry=cn_registry)
    return custom


@app.route("/metrics/stocks")
def stock_metrics():
    return generate_latest(registry=stocks_registry)


@app.route("/metrics/dynamic")
def dynamic_metrics():
    reg = CollectorRegistry()
    return generate_latest(registry=reg)


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
from e_insight.crawler.spiders.east_money import EastMoney


def scheduler():
    print("scheduler started.")
    LOG.info("scheduler started.")
    schedule.every(30).seconds.do(ping)
    schedule.every(20).seconds.do(start_crawl, EastMoney)
    schedule.every(5).minutes.do(start_crawl, USABond)

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
