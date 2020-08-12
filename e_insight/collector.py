import time
from prometheus_client import Counter, Gauge, Summary, Histogram, Info, Enum
from e_insight.stocks.sina import Stock, Quote
from e_insight.bonds import usa
from e_insight.lib.cache import cache
from e_insight.index import rate
from e_insight.index import currency

now = Gauge('now', 'time now for test')

sh000300 = Gauge("sh000300", "沪深 300 指数")
sh600519 = Gauge("sh600519", "茅台")
sh000001 = Gauge("sh000001", "上证指数")

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

cn_1year_rate = Gauge("CN_1YEAR_RATE", "中国一年期存款利率")
cn_cpi_incr = Gauge("CN_CPI_INC", "中国 CPI 增长率")
lpr_1year = Gauge("LPR_1YEAR", "lpr 1 年期")
lpr_5year = Gauge("LPR_5YEAR", "lpr 5 年期")

last_shibor = Gauge("SHIBOR_LAST_NIGHT", "隔夜拆借利率")
week_1_shibor = Gauge("SHIBOR_1WEEK", "1 周 拆借利率")
week_2_shibor = Gauge("SHIBOR_2WEEK", "2 周 拆借利率")
mon_1_shibor = Gauge("SHIBOR_1MON", "1 月 拆借利率")
mon_3_shibor = Gauge("SHIBOR_3MON", "3 月 拆借利率")
mon_6_shibor = Gauge("SHIBOR_6MON", "6 月 拆借利率")
mon_9_shibor = Gauge("SHIBOR_9MON", "9 月 拆借利率")
year_1_shibor = Gauge("SHIBOR_1YEAR", "1 年 拆借利率")

saving_rate_current = Gauge("SAVING_RATE_CUR", "活期存款利率")
saving_rate_3mon = Gauge("SAVING_RATE_3MON", "3 月存款利率")
saving_rate_6mon = Gauge("SAVING_RATE_6MON", "6 月存款利率")

saving_rate_1year = Gauge("SAVING_RATE_1YEAR", "1 年存款利率")
saving_rate_2year = Gauge("SAVING_RATE_2YEAR", "2 年存款利率")
saving_rate_3year = Gauge("SAVING_RATE_3YEAR", "3 年存款利率")
saving_rate_5year = Gauge("SAVING_RATE_5YEAR", "5 年存款利率")

loan_rate_6mon = Gauge("LOAN_RATE_6MON", "6 月贷款利率")
loan_rate_1year = Gauge("LOAN_RATE_1YEAR", "1 年贷款利率")
loan_rate_3year = Gauge("LOAN_RATE_3YEAR", "3 年贷款利率")
loan_rate_5year = Gauge("LOAN_RATE_5YEAR", "5 年贷款利率")
loan_rate_10year = Gauge("LOAN_RATE_10YEAR", "10 年贷款利率")

m2 = Gauge("M2", "M2 供应量")
m1 = Gauge("M1", "M1 供应量")
m0 = Gauge("M0", "M0 供应量")

m2_inc = Gauge("M2_INC", "M2 同比增长量")
m1_inc = Gauge("M1_INC", "M1 同比增长量")
m0_inc = Gauge("M0_INC", "M0 同比增长量")

reserve_rate_pre = Gauge("RESERVE_RATE_PRE", "存款准备金率前期")
reserve_rate = Gauge("RESERVE_RATE", "存款准备金率")

reserve_rate_mid_pre = Gauge("RESERVE_RATE_MIDPRE", "中小金融存款准备金率前期")
reserve_rate_mid = Gauge("RESERVE_RATE_MID", "中小金融存款准备金率")

# ['Counter', 'Gauge', 'Summary', 'Histogram', 'Info', 'Enum']
# A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero on restart. For example, you can use a counter to represent the number of requests served, tasks completed, or errors.
# A gauge is a metric that represents a single numerical value that can arbitrarily go up and down.
# A histogram samples observations (usually things like request durations or response sizes) and counts them in configurable buckets. It also provides a sum of all observed values.


def init_metrics_collectors():
    # register func for metrics
    now.set_function(lambda: int(time.time()))
    sh000300.set_function(
        cache(60)(lambda: Stock(sh000300._documentation, sh000300._name).get(
            "current")))

    sh600519.set_function(
        cache(60)(lambda: Stock(sh600519._documentation, sh600519._name).get(
            "current")))

    sh000001.set_function(
        cache(60)(lambda: Stock(sh000001._documentation, sh000001._name).get(
            "current")))

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

    cn_1year_rate.set_function(lambda: rate.fetch_rate())
    cn_cpi_incr.set_function(lambda: rate.fetch_cpi())

    lpr_1year.set_function(lambda: rate.fetch_lpr("1Y"))
    lpr_5year.set_function(lambda: rate.fetch_lpr("5Y"))

    last_shibor.set_function(lambda: rate.fetch_shibor("隔夜(O/N)"))
    week_1_shibor.set_function(lambda: rate.fetch_shibor("1周"))
    week_2_shibor.set_function(lambda: rate.fetch_shibor("2周"))
    mon_1_shibor.set_function(lambda: rate.fetch_shibor("1个月"))
    mon_3_shibor.set_function(lambda: rate.fetch_shibor("3个月"))
    mon_6_shibor.set_function(lambda: rate.fetch_shibor("6个月"))
    mon_9_shibor.set_function(lambda: rate.fetch_shibor("9个月"))
    year_1_shibor.set_function(lambda: rate.fetch_shibor("1年"))

    saving_rate_current.set_function(lambda: rate.fetch_savingrate("活期存款"))
    saving_rate_3mon.set_function(lambda: rate.fetch_savingrate("3个月"))
    saving_rate_6mon.set_function(lambda: rate.fetch_savingrate("6个月"))
    saving_rate_1year.set_function(lambda: rate.fetch_savingrate("1年(整存整取)"))
    saving_rate_2year.set_function(lambda: rate.fetch_savingrate("2年(整存整取)"))
    saving_rate_3year.set_function(lambda: rate.fetch_savingrate("3年(整存整取)"))
    saving_rate_5year.set_function(lambda: rate.fetch_savingrate("5年(整存整取)"))

    loan_rate_6mon.set_function(lambda: rate.fetch_loanrate("6个月以内(含)"))
    loan_rate_6mon.set_function(lambda: rate.fetch_loanrate("6个月至1年(含)"))
    loan_rate_1year.set_function(lambda: rate.fetch_loanrate("6个月至1年(含)"))
    loan_rate_3year.set_function(lambda: rate.fetch_loanrate("1至3年(含)"))
    loan_rate_5year.set_function(lambda: rate.fetch_loanrate("3至5年(含)"))
    loan_rate_10year.set_function(lambda: rate.fetch_loanrate("5年以上"))

    m0.set_function(currency.fetch_M0)
    m1.set_function(currency.fetch_M1)
    m2.set_function(currency.fetch_M2)
    m0_inc.set_function(currency.fetch_M0_Inc)
    m1_inc.set_function(currency.fetch_M1_Inc)
    m2_inc.set_function(currency.fetch_M2_Inc)

    reserve_rate_pre.set_function(currency.fetch_reserve_rate_pre)
    reserve_rate.set_function(currency.fetch_reserve_rate)

    reserve_rate_mid.set_function(currency.fetch_mid_reserve_rate)
    reserve_rate_mid_pre.set_function(currency.fetch_mid_reserve_rate_pre)


init_metrics_collectors()

us_macro_collectors = [
    bc1month, bc2month, bc3month, bc6month, bc1year, bc2year, bc3year, bc5year,
    bc7year, bc10year, bc20year, bc30year
]

cn_macro_collectors = [
    saving_rate_current, saving_rate_3mon, saving_rate_6mon, saving_rate_1year,
    saving_rate_2year, saving_rate_3year, saving_rate_5year, loan_rate_6mon,
    loan_rate_1year, loan_rate_3year, loan_rate_5year, loan_rate_10year, m0,
    m1, m2, m0_inc, m1_inc, m2_inc, cn_1year_rate, cn_cpi_incr, lpr_1year,
    lpr_5year, last_shibor, week_1_shibor, week_2_shibor, mon_1_shibor,
    mon_3_shibor, mon_6_shibor, mon_9_shibor, year_1_shibor, reserve_rate,
    reserve_rate_pre, reserve_rate_mid, reserve_rate_mid_pre
]

stocks_collectors = [sh000300, sh600519, sh000001]
