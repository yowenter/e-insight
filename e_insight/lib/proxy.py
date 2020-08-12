import requests
import os
from e_insight.lib.cache import cache

PROXY = os.getenv("DOWNLOADER_PROXY", "http://localhost:8080/fetch")


@cache(600)
def fetch_html(url):
    resp = requests.get(PROXY, params={"url": url}).text
    return resp
