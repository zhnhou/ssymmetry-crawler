# -*-coding:utf8-*-#

__author__ = 'HZ'

'''
created at 14:52 07/24/2017
'''

import re,os
import time, json
import redis
from scrapy import Request
from ConfigParser import ConfigParser
from .. import items
from scrapy_redis.spiders import RedisSpider
from .. import settings

class babytree(RedisSpider):
    name = 'babytree'

    allowed_domains = ["meitun.com"]

    start_urls = ['http://www.meitun.com/loadfc?callback=callback']

    def __init__(self):
        
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")

        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

        r.delete(self.name + ":start_urls")
        r.rpush('babytree:start_urls', *self.start_urls)

        r.delete(self.name + ":dupefilter")
        r.delete(self.name + ":items")
        r.delete(self.name + ":requests")

    def parse(self, response):
    
        tmp = response.body
        tmp = tmp[tmp.find("(")+1:tmp.find(")")]
        response = response.replace(body=tmp)
        del tmp
        
        js = json.loads(response.body)
        
        meitun_item_URL = "http://search.meitun.com/search/itempage?key=&fcategid=@id@&pageSize=20&pageNo=@pageSize@&slprice=0&salesvolume=0&hasInventoryOnly=0&brandid=&specificationid="

        # http://www.meitun.com/loadfc?callback=callback

        for main in js['data']:
            for cat in main['childs']:
                if 'id' in cat:
                    # cat['id'] is int, why?
                    url = meitun_item_URL.replace("@id@", str(cat['id'])).replace("@pageSize@","1")

                    yield Request(url, callback=self.parse_index_page, priority=1, meta={'category':cat['name']})
