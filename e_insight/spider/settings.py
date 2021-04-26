settings = {'LOG_LEVEL': 'DEBUG',
            'COOKIES_ENABLED': True,
            'DOWNLOADER_MIDDLEWARES': {
                'e_insight.spider.proxy.ChromeProxy': 400
            },
            "ITEM_PIPELINES": {
                'e_insight.spider.pipeline.PrometheusMetricItemPipeline': 800
            }
            }
