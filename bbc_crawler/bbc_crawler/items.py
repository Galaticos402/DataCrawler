# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BccCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# class NewsCrawlerItem(scrapy.Item):
#     title = scrapy.Field()
#     author = scrapy.Field()


# class LaptopCrawlerItem(scrapy.Item):
#     name = scrapy.Field()
#     price = scrapy.Field()


class CoinGeckoCrawlerItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    marketCap = scrapy.Field()
    dayTradingVolume = scrapy.Field()
