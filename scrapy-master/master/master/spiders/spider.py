from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from master.items import MasterItem


class myspider(CrawlSpider):

    name = 'master'
    # allowed_domains = ['58.com']
    item = MasterItem()
    start_urls = ['https://movie.douban.com/top250?']
    rules = (
        #https://movie.douban.com/top250?start=225&filter=
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250?.*?',)), callback='parse_item',
             follow=True),
    )

    def parse_item(self,response):
        item = self.item
        print(item)
        item['url'] = response.url
        return item