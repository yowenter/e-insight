import random
from prometheus_client import Counter, Gauge, Summary, Histogram, Info, Enum
from e_insight.stocks.sina import Stock


rand = Gauge('random', 'random 0~1 for test')

sh000300 = Gauge("sh000300", "沪深 300 指数")


# ['Counter', 'Gauge', 'Summary', 'Histogram', 'Info', 'Enum']
# A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero on restart. For example, you can use a counter to represent the number of requests served, tasks completed, or errors.
# A gauge is a metric that represents a single numerical value that can arbitrarily go up and down.
# A histogram samples observations (usually things like request durations or response sizes) and counts them in configurable buckets. It also provides a sum of all observed values.

def simple_random():
    return random.random()

def register_metrics_func():
    # register func for metrics
    rand.set_function(simple_random)
    sh000300.set_function(lambda : Stock("沪深300", sh000300._name).get("current"))



register_metrics_func()
ALL_COLLECTORS = [rand, sh000300]








