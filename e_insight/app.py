from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app, CollectorRegistry, MetricsHandler, generate_latest

from e_insight.collector import ALL_COLLECTORS
from e_insight.utils.cache import cache

# Create my app
app = Flask(__name__)


# Init Collector registry
registry = CollectorRegistry()


for c in ALL_COLLECTORS:
    registry.register(c)






@app.route("/metrics")
def metrics():
    # todo use cronjob to refresh cache
    return generate_latest(registry=registry)


# gunicorn e_insight.app:app_dispatch
# gunicorn --log-level debug  e_insight.app:app_dispatch --reload -w 1 --bind 0.0.0.0


if __name__ == '__main__':
#    app.run(debug=True, port=5050)
    app.run()