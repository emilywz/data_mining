# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class SoPipeline(ImagesPipeline):
    # 重写get_media_requests()方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_link'],
            meta={'name':item['img_title']}
        )

    # 重写file_path方法
    def file_path(self, request, response=None, info=None):
        # 请求对象的meta属性 <==> Request(meta={})
        # 请求对象的url属性 <==> Request(url='')
        filename = request.meta['name'] + '.' + request.url.split('.')[-1]

        return filename








