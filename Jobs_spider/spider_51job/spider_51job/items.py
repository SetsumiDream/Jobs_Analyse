# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider51JobItem(scrapy.Item):

    workname = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    cptype = scrapy.Field()
    business = scrapy.Field()
    place = scrapy.Field()
    exp = scrapy.Field()
    edu = scrapy.Field()
    needNum = scrapy.Field()
    time = scrapy.Field()
    work_msg = scrapy.Field()
