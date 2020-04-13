# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from youy.items import YouyItem
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider  #引入RedisCrawlSpider类
# class DyttSlaverSpider(CrawlSpider):
class DemoSpider(RedisCrawlSpider):
    name = 'master'

    # allowed_domains = ['douban.com']
    # start_urls = ['https://movie.douban.com/top250']
    # start_urls=['http://www.youyuan.com/find/beijing/mm18-0/advance-0-0-0-0-0-0-0/p1/']
    redis_key = "your:start_urls"
    rules = (
        # Rule(LinkExtractor(allow=r'/advance-0-0-0-0-0-0-0/p\d+/'), follow=False),
        #http://www.youyuan.com/969499271-profile/
        Rule(LinkExtractor(allow=r'/\d+-profile/'), callback='parse_item', follow=False),
    )

    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(DemoSpider, self).__init__(*args, **kwargs)
    def parse_item(self, response):
           item=YouyItem()
           container={}
           container["name"] = \
           response.xpath('//dl[@class="personal_cen"]//div[@class="main"]/strong/text()').extract()[0]
           container["ads"] = response.xpath('//dl[@class="personal_cen"]//dd/p/text()').extract()[0]
           item=container
           print(response.url)
           print("*"*50 )
           yield item
           pass
