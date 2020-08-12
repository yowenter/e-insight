import re
from e_insight.lib.proxy import fetch_html
from e_insight.lib.catch import catch_default
from bs4 import BeautifulSoup as Soup


# html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
# soup = Soup(html)
#
# # M1
# soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
#

#


@catch_default(-1)
def fetch_M2():
    html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
    soup = Soup(html, features="html.parser")
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[0].text).group())


@catch_default(-1)
def fetch_M2_Inc():
    html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[1].text).group())


@catch_default(-1)
def fetch_M1():
    html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[3].text).group())


@catch_default(-1)
def fetch_M1_Inc():
    html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[4].text).group())


@catch_default(-1)
def fetch_M0():
    html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[6].text).group())


@catch_default(-1)
def fetch_M0_Inc():
    html = fetch_html("https://data.eastmoney.com/cjsj/hbgyl.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[7].text).group())


@catch_default(-1)
def fetch_reserve_rate_pre():
    html = fetch_html("http://data.eastmoney.com/cjsj/ckzbj.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[1].text).group())


@catch_default(-1)
def fetch_reserve_rate():
    html = fetch_html("http://data.eastmoney.com/cjsj/ckzbj.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[2].text).group())


@catch_default(-1)
def fetch_mid_reserve_rate():
    html = fetch_html("http://data.eastmoney.com/cjsj/ckzbj.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[5].text).group())


@catch_default(-1)
def fetch_mid_reserve_rate_pre():
    html = fetch_html("http://data.eastmoney.com/cjsj/ckzbj.html")
    soup = Soup(html)
    siblings = soup.find("td", attrs={"style": "width:;"}).find_next_siblings()
    return float(re.search(r"(\w|\.)+", siblings[4].text).group())
