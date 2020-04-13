from scrapy import cmdline
# cmdline.execute("scrapy crawl dytt_slaver -o a.json -s FEED_EXPORT_ENCODING=utf-8".split())
cmdline.execute("scrapy crawl dytt_slaver".split())