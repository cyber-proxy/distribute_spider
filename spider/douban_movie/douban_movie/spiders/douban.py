# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("../")
from douban_movie.items import *

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        for info in response.xpath('//div[@class="item"]'):
            item = DoubanMovieItem()
            item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
            item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
            item['link'] = info.xpath('div[@class="pic"]/a/@href').extract
            yield item

            next_page = response.xpath('//span[@class="next"]/a/@href')
            if next_page:
                url = response.urljoin(next_page[0].extract())
                yield scrapy.Request(url, self.parse)
        pass
