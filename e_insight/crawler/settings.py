settings = {'LOG_LEVEL': 'DEBUG',
            'COOKIES_ENABLED': True,
            'DOWNLOADER_MIDDLEWARES': {
                'e_insight.crawler.proxy.ChromeProxy': 400
            },
            "ITEM_PIPELINES": {
                'e_insight.crawler.pipeline.PrometheusMetricItemPipeline': 800
            }
            }
