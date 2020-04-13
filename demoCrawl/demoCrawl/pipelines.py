# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
class DemocrawlPipeline(object):
    def __init__(self):
        self.redis_url = 'redis://127.0.0.1:6379/'
        self.r = redis.Redis.from_url(self.redis_url, decode_responses=True)

    def process_item(self, item, spider):
        self.r.lpush('myredis:start_urls', item['url'])
