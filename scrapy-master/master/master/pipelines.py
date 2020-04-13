import redis

class MasterPipeline(object):

    def __init__(self):
        self.redis_url=redis.Redis(host="localhost",port=6379)
        self.r = redis.Redis.from_url(self.redis_url)

    def process_item(self, item, spider):
        self.r.lpush('myredis:start_urls', item['url'])