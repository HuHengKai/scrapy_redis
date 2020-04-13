from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/finish']

    rules = [
        Rule(LinkExtractor(
            restrict_css=('.book-info')
        ), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }
        print('----------------')
        print(response.url)