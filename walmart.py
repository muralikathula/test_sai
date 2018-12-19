import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.selector import Selector
import MySQLdb
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class walmart(scrapy.Spider):
    name = "walmart"
    handle_httpstatus_list = [403]

    def __init__(self):
        self.conn = MySQLdb.connect(db= "walmart", host = "127.0.0.1", user="root", passwd = "123", use_unicode=True, charset="utf8mb4")
        self.cursor = self.conn.cursor()
        dispatcher.connect(self.mysql_conn_close, signals.spider_closed)

    def mysql_conn_close(self, spider):
        self.conn.commit()
        self.conn.close()

    def start_requests(self):
        url = 'https://www.walmart.com/browse/clothing/t-shirts-tank-tops/5438_133197_4237948'
        headers = {
                ':method': 'GET',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'upgrade-insecure-requests': 1,
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
                }
    
        yield FormRequest(url,callback=self.parse_next, headers=headers)

    def parse_next(self,response):
        import pdb;pdb.set_trace()

