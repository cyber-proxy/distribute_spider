# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Spider, Request
import sys
# sys.path.append("..\..")
from zhihu.items import ZhihuItem

class ZhihuSpiderSpider(scrapy.Spider):
    name = 'zhihu_spider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user = "excited-vczh"

    user_url = "https://www.zhihu.com/people/{user}/answers?include={include}"
    user_query = "locations, employments, gender"

    follows_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)

    def parse(self, response):
        pass

    def parse_user(self, response):
        result = json.loads(response.text)
        item = ZhihuItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item