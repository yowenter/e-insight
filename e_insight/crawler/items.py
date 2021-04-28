import scrapy


class MetricItem(scrapy.item.Item):
    name = scrapy.Field()
    value = scrapy.Field()
    type = scrapy.Field()
    description = scrapy.Field()
    labels = scrapy.Field()
