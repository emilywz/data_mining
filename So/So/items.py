# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoItem(scrapy.Item):
    # define the fields for your item here like:
    # 图片链接 - 必须给管道(scrapy的图片管道类使用)
    img_link = scrapy.Field()
    img_title = scrapy.Field()







