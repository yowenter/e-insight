import requests
import logging

LOG = logging.getLogger(__name__)

DEFAUTL_TIMEOUT =10

class Stock(object):

    url_format="http://hq.sinajs.cn/list={stock_no}"
    data_idx = {
        "open":1,
        "closed":2,
        "current":3,
        "max":4,
        "min":5
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
        return points[self.data_idx[idx]]

    
    def get(self, idx):
        resp = self.fetch()
        if not resp:
            return 
        return self.parse(resp, idx)


    
    @property
    def url(self):
        return self.url_format.format(stock_no=self.no)

        

# if __name__=='__main__':
#     s = Stock("沪深300", 'sh000300')
#     print(s.get("current"))

    






