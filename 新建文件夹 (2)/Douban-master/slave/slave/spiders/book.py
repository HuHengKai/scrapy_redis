# -*- coding: utf-8 -*-
import scrapy,re
from slave.items import SlaveItem
from scrapy_redis.spiders import RedisSpider

class BookSpider(RedisSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    #start_urls = ['http://book.douban.com/']
    redis_key = 'myredis:start_urls'

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(BookSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        item = SlaveItem()
        # names={}
        # print('='*20, response.status)
        # pass
        # # divs=response.xpath('//div[@class="cover"]/a/@title').getall()
        item["title"]=response.xpath('//h1[1]//text()').get()
        item['author']="fdfdgfgfgfgfggf"
        yield item

        #
        #
        # item['title'] = vo.css('#wrapper h1 span::text').extract_first()
        #
        #
        #
        # authors = re.search('<span.*?作者.*?</span>(.*?)<br>', info,re.S).group(1)
        #
        # yield item
