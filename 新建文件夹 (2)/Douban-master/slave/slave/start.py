from scrapy import cmdline
cmdline.execute("scrapy crawl book -o a.json".split())