from flask import Flask
from prometheus_client import CollectorRegistry, generate_latest

from e_insight import collector

# Create my app
app = Flask(__name__)

# Init Collector registry
registry = CollectorRegistry()

for c in collector.ALL_COLLECTORS:
    registry.register(c)


@app.route("/metrics")
def metrics():
    # todo use cronjob to refresh cache
    # system = generate_latest()
    custom = generate_latest(registry=registry)
    return custom


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


# gunicorn e_insight.app:app_dispatch
# gunicorn --log-level debug  e_insight.app:app_dispatch --reload -w 1 --bind 0.0.0.0


if __name__ == '__main__':
    #    app.run(debug=True, port=5050)
    app.run()
