import logging
import os

LOG = logging.getLogger(__name__)

PROXY = os.getenv("DOWNLOADER_PROXY", "http://localhost:8080/fetch")


class ChromeProxy:
    def process_request(self, request, spider):
        if getattr(spider, "use_chrome_proxy", False):
            LOG.info("spider %s use chrome proxy %s", spider.name, request.url)
            request.url = "%s?url=%s" % (PROXY, request.url)
        else:
            LOG.info("spider %s not use chrome proxy", spider.name)
