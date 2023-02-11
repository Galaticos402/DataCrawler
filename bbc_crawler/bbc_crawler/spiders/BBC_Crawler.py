import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import  CoinGeckoCrawlerItem
import time

class BBC_Crawler(CrawlSpider):
    urlSeen = []
    name = 'bbc_crawler'
    allowed_domains = ['www.coingecko.com']
    start_urls = ['https://www.coingecko.com/']
    rules = (
        Rule(LinkExtractor(allow='/en/coins/'), callback='parse_item_news'),
        Rule(LinkExtractor(allow='/?page'), follow=True, )
    )

    # def parse_next(self, response):
    #     if response.

    def parse_item_news(self, response):
        time.sleep(1)
        item = CoinGeckoCrawlerItem()
        item['name'] = response.xpath('/html/body/div[5]/div[5]/div[1]/div/div[1]/div[2]/h1/span[1]/text()').extract()[0].replace("\n","")
        item['price'] = response.xpath('/html/body/div[5]/div[5]/div[1]/div/div[1]/div[3]/div/div[1]/span[1]/span/text()').extract()[0]
        item['marketCap'] = response.xpath('/html/body/div[5]/div[5]/div[1]/div/div[2]/div[2]/div[1]/div[1]/span[2]/span/text()').extract()[0]
        item['dayTradingVolume'] = response.xpath('/html/body/div[5]/div[5]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span[2]/span/text()').extract()[0]
        yield item


