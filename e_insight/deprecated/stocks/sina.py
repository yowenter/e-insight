import requests
import logging

LOG = logging.getLogger(__name__)

DEFAUTL_TIMEOUT = 10


class Stock(object):
    url_format = "http://hq.sinajs.cn/list={stock_no}"
    data_idx = {
        "open": 1,
        "closed": 2,
        "current": 3,
        "max": 4,
        "min": 5
    }

    # var hq_str_sh000300="沪深300,3675.2642,3678.3921,3669.3703,3695.4646,3650.0537,0,0,184810220,206010958185,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2019-02-28,15:01:50,00";

    def __init__(self, name, stock_no):
        self.name = name
        self.no = stock_no

    def fetch(self):
        try:
            resp = requests.get(self.url, timeout=DEFAUTL_TIMEOUT)
        except Exception as e:
            LOG.warn("Fetch url %s error %s", self.url, str(e))
        else:
            return resp.text

    def parse(self, text, idx=None):
        _, data = text.split("=")
        points = data.strip().split(",")
        LOG.debug("Points %s", points)
        return points[self.data_idx[idx]]

    def get(self, idx):
        resp = self.fetch()
        if not resp:
            return
        return self.parse(resp, idx)

    @property
    def url(self):
        return self.url_format.format(stock_no=self.no)


class Quote(Stock):
    # https://hq.sinajs.cn/list=SC1904
    # var hq_str_SC1904="原油1904,231830,440.40,442.80,439.80,439.70,441.80,441.90,441.80,441.50,441.50,12,52,46390,88892,沪,原油,2019-02-28,1,460.700,427.600,467.900,427.600,467.900,414.100,467.900,356.400,10.449";
    data_idx = {
        "open": 2,
        "closed": 5,
        "current": 7,
        "max": 3,
        "min": 4
    }
    url_format = "https://hq.sinajs.cn/list={stock_no}"

# if __name__=='__main__':
#     s = Stock("沪深300", 'sh000300')
#     print(s.get("current"))
