# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&t1=595&src=banner_beauty&sn={}&listtype=new&temp=1'

    def start_requests(self):
        for sn in range(0,121,30):
            url = self.url.format(sn)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        html_json = json.loads(response.text)
        item = SoItem()
        for img_dict in html_json['list']:
            item['img_link'] = img_dict['qhimg_url']
            item['img_title'] = img_dict['title']

            yield item








