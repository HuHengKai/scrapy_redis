# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from demoCrawl.items import DemocrawlItem



class BaiduSpider(CrawlSpider):
    name = 'baidu'
    # allowed_domains = ['baidu.com']
    # start_urls = ['https://book.douban.com/']
    start_urls=['https://book.douban.com/tag/%E6%BC%AB%E7%94%BB']
    rules = (
                # https: // book.douban.com / tag / % E5 % B0 % 8F % E8 % AF % B4
        # Rule(LinkExtractor(allow=r'tag/.*?'), callback='parse_item', follow=True),
        # https: // book.douban.com / subject / 10554308 /
        Rule(LinkExtractor(allow=r'/subject/(\d+)/',deny=("=","buylinks")), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item=DemocrawlItem()
        item['url']=response.url
        return item
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print(response.url)