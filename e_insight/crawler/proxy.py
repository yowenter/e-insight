import logging
import os

LOG = logging.getLogger(__name__)

PROXY = os.getenv("DOWNLOADER_PROXY", "http://localhost:8080/fetch")


class ChromeProxy:
    def process_request(self, request, spider):
        if getattr(spider, "use_chrome_proxy", False):
            LOG.info("crawler %s use chrome proxy %s", spider.name, request.url)
            request.replace(url="%s?url=%s" % (PROXY, request.url))
        else:
            LOG.info("crawler %s not use chrome proxy", spider.name)
