# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WxappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    work = scrapy.Field()
    place = scrapy.Field()
    salary = scrapy.Field()
    time = scrapy.Field()


    # 如果要下载图片要定义这个字段，然后setting里注册ImagesPipeline
    # 图片路径也要配置
    # 一般要重写这个类
    #
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
