import time
from prometheus_client import Counter, Gauge, Summary, Histogram, Info, Enum
from e_insight.stocks.sina import Stock, Quote
from e_insight.bonds import usa
from e_insight.lib.cache import cache

now = Gauge('now', 'time now for test')

sh000300 = Gauge("sh000300", "沪深 300 指数")

sc1904 = Gauge('SC1904', "原油期货")

bc1month = Gauge('BC_1MONTH', '美国 1 月期国债利率')
bc2month = Gauge('BC_2MONTH', '美国 2 月期国债利率')
bc3month = Gauge('BC_3MONTH', '美国 3 月期国债利率')
bc6month = Gauge('BC_6MONTH', '美国 6 月期国债利率')

bc1year = Gauge('BC_1YEAR', '美国 1 年期国债利率')
bc2year = Gauge('BC_2YEAR', '美国 2 年期国债利率')
bc3year = Gauge('BC_3YEAR', '美国 3 年期国债利率')
bc5year = Gauge('BC_5YEAR', '美国 5 年期国债利率')
bc7year = Gauge('BC_7YEAR', '美国 7 年期国债利率')
bc10year = Gauge('BC_10YEAR', '美国 10 年期国债利率')
bc20year = Gauge('BC_20YEAR', '美国 20 年期国债利率')
bc30year = Gauge('BC_30YEAR', '美国 30 年期国债利率')


# ['Counter', 'Gauge', 'Summary', 'Histogram', 'Info', 'Enum']
# A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero on restart. For example, you can use a counter to represent the number of requests served, tasks completed, or errors.
# A gauge is a metric that represents a single numerical value that can arbitrarily go up and down.
# A histogram samples observations (usually things like request durations or response sizes) and counts them in configurable buckets. It also provides a sum of all observed values.


def init_metrics_collectors():
    # register func for metrics
    now.set_function(lambda: int(time.time()))
    sh000300.set_function(cache(180)(lambda: Stock("沪深300", sh000300._name).get("current")))

    bc1month.set_function(lambda: usa.get_bond("BC_1MONTH"))
    bc2month.set_function(lambda: usa.get_bond("BC_2MONTH"))
    bc3month.set_function(lambda: usa.get_bond("BC_3MONTH"))
    bc6month.set_function(lambda: usa.get_bond("BC_6MONTH"))
    bc1year.set_function(lambda: usa.get_bond("BC_1YEAR"))
    bc2year.set_function(lambda: usa.get_bond("BC_2YEAR"))
    bc3year.set_function(lambda: usa.get_bond("BC_3YEAR"))
    bc5year.set_function(lambda: usa.get_bond("BC_5YEAR"))
    bc7year.set_function(lambda: usa.get_bond("BC_7YEAR"))
    bc10year.set_function(lambda: usa.get_bond("BC_10YEAR"))
    bc20year.set_function(lambda: usa.get_bond("BC_20YEAR"))
    bc30year.set_function(lambda: usa.get_bond("BC_30YEAR"))

    return [now, sh000300, bc1month, bc2month, bc3month, bc6month, bc1year, bc2year, bc3year, bc5year, bc7year,
            bc10year, bc20year, bc30year]

    # sc1904.set_function(lambda: Quote("原油期货", sc1904._name).get("current"))


ALL_COLLECTORS = init_metrics_collectors()
