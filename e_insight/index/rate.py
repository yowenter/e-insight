from e_insight.lib.proxy import fetch_html
from e_insight.lib.catch import catch_default
from bs4 import BeautifulSoup as Soup


# html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
# soup = Soup(html)
#
# # 中国一年期存款利率
# soup.find("td", text="1年期存款利率").find_next_sibling().text
#

#
# # CPI
# soup.find("td", text="1年期存款利率").find_next_siblings()[5]


# # LPR 1 年期利率
# soup.find("td", text="1Y").find_next_sibling().text
#
# # LPR 5 年期利率
# soup.find("td", text="5Y").find_next_sibling().text


# shibor

@catch_default(-1)
def fetch_rate():
    html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
    soup = Soup(html)
    return float(soup.find("td", text="1年期存款利率").find_next_sibling().text)


@catch_default(-1)
def fetch_cpi():
    html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
    soup = Soup(html)
    return float(soup.find("td", text="1年期存款利率").find_next_siblings()[5].text)


@catch_default(-1)
def fetch_lpr(yield_term):
    html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
    soup = Soup(html)
    return float(soup.find("td", text=yield_term).find_next_sibling().text)


@catch_default(-1)
def fetch_shibor(yield_term):
    html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
    soup = Soup(html)
    return float(soup.find("td", text=yield_term).find_next_sibling().text)


@catch_default(-1)
def fetch_savingrate(yield_term):
    html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
    soup = Soup(html)
    return float(soup.find("td", text=yield_term).find_next_sibling().text)


@catch_default(-1)
def fetch_loanrate(yield_term):
    html = fetch_html("http://data.eastmoney.com/cjsj/globalRate.html")
    soup = Soup(html)
    return float(soup.find("td", text=yield_term).find_next_sibling().text)

# soup.find("td", text="隔夜(O/N)").find_next_sibling().text
#
# soup.find("td", text="1周").find_next_sibling().text
#
# soup.find("td", text="2周").find_next_sibling().text
#
# soup.find("td", text="1个月").find_next_sibling().text
#
# soup.find("td", text="3个月").find_next_sibling().text
#
# soup.find("td", text="6个月").find_next_sibling().text
#
# soup.find("td", text="9个月").find_next_sibling().text
#
# soup.find("td", text="1年").find_next_sibling().text
