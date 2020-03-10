# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# scrapy imagepipeline
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class SoPipeline(ImagesPipeline):
    # rewrite get_media_requests()
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_link'],
            meta={'name':item['img_title']}
        )


    def file_path(self, request, response=None, info=None):
        #rewrite file_path()
        filename = request.meta['name'] + '.' + request.url.split('.')[-1]

        return filename








