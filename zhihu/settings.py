# -*- coding:utf-8 -*-

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

LOG_FILE = 'zhihu.log'
LOG_LEVEL= 'INFO'

COOKIES_DEBUG = False
RETRY_ENABLED = False
REDIRECT_ENABLED = False

DEPTH_LIMIT=0
DEPTH_PRIORITY=0

CONCURRENT_ITEMS = 1000
CONCURRENT_REQUESTS = 100
#The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain.
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 0
CONCURRENT_REQUESTS_PER_SPIDER=100

DNSCACHE_ENABLED = True

DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 10

ITEM_PIPELINES = {
    'zhihu.pipelines.DoNothingPipeline': 300,
    #'zhihu.pipelines.JsonWithEncodingPipeline': 300,
    #'zhihu.pipelines.MongoDBPipeline': 300,
    }

DOWNLOADER_MIDDLEWARES = {
    'zhihu.misc.middleware.CustomHttpProxyMiddleware': 80,
    #'zhihu.misc.middleware.CustomUserAgentMiddleware': 81,
    }

SCHEDULER_ORDER = 'BFO'

HEADER={
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Referer": "https://www.zhihu.com/people/leo-63-45",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
    }

COOKIES={
    '_za':r'95040d03-2ca8-4d28-9d98-3e2caab7d4b0',
    'udid':r'"AEDAH5rdnAmPTrUDiMA9PuE0bR4JkgIH4AI=|1457925897"',
    'd_c0':r'"ADBAnbvzpQmPTkk4T7ZN22DicGYkFNkbamc=|1461306652"',
    '_zap':r'350248ee-cbfd-4d66-be65-4b30d8512c00',
    '_xsrf':r'daab34f2c2dd94f7f45c412d224e3526',
    'q_c1':r'a6a6b6b5a39f4e6eaaff4f9a79cc78f7|1470298611000|1470298611000',
    '__utma':r'51854390.765533428.1465804053.1470216647.1470298874.31',
    '__utmb':r'51854390.25.9.1470298963991',
    '__utmc':r'51854390',
    '__utmz':r'51854390.1470216647.30.29.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__utmv':r'51854390.000--|2=registration_date=20160328=1^3=entry_date=20160804=1',
    'z_c0':r'Mi4wQUZEQUNpSlJyd2tBTUVDZHVfT2xDUmNBQUFCaEFsVk5fNG5LVndDSFdwLU5jZFJMb3IwcUJfMEpTckRMc1RoT0lR|1470299391|b234c66294689940873218f4c118b5b1db97d4b4',
    'cap_id':r'"YmEyOTg0MzI4ZDM3NDA4MDljODJkYWM5ZWQ1MmU3ZDg=|1470299391|72a82888609bc74ee8bdd396240bc8edd9b5adeb"',
    'l_cap_id':r'"NWE1YjhlYjk5OTY1NDQ0NjljNjE3ZDhlMmM5Yzk3N2Y=|1470299391|e839798c0636a5ed8bcd78b85bd77161aef20916"',
    'login':r'"ZDc1NjM5Mjk0YzAwNGE2NThlZjRkYjJkMjMyM2EyMjA=|1470299391|ff34d61db4f435dc3627d11199b5e2bb2f3c4806"',
    'n_c':r'1',
    }

