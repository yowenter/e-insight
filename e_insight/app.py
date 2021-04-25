from flask import Flask
from prometheus_client import CollectorRegistry, generate_latest

from e_insight import collector

# Create my app
app = Flask(__name__)

# Init Collector registry
registry = CollectorRegistry()

cn_registry = CollectorRegistry()

stocks_registry = CollectorRegistry()

for c in collector.us_macro_collectors:
    registry.register(c)

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


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


# gunicorn e_insight.app:app_dispatch
# gunicorn --log-level debug  e_insight.app:app_dispatch --reload -w 1 --bind 0.0.0.0

from e_insight.spider import p

#
# thread = Thread(target=lambda: p.start)

from multiprocessing import Process

proc = Process(target=lambda: p.start, daemon=True)
proc.start()
if __name__ == '__main__':
    #    app.run(debug=True, port=5050)

    app.run()
