# -*- coding: utf-8 -*-

# Scrapy settings for beibei project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'babytree'

SPIDER_MODULES = ['babytree.spiders']
NEWSPIDER_MODULE = 'babytree.spiders'

ROBOTSTXT_OBEY=False

LOG_LEVEL = 'INFO'

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0.5


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'babytree.spiders.rotate_useragent.RotateUserAgentMiddleware': 400
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
}

#Redis
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True
#
# # Schedule requests using a priority queue. (default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#
# #slave
REDIS_HOST = '127.0.0.1' #dev
REDIS_PORT = 6379
TELNETCONSOLE_PORT = None

# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# Schedule requests using a queue (FIFO).
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

