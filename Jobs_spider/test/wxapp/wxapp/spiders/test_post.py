# -*- coding: utf-8 -*-
import json

import scrapy


class TestPostSpider(scrapy.Spider):
    name = 'test_post'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    '''
    def parse(self, response):

        url = 'https://fanyi.baidu.com/sug'

        formdata = {
            'kw': 'job'
        }

        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.get_json_data)
    '''

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        formdata = {
            'kw': 'job'
        }
        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.get_json_data)

    def get_json_data(self, response):

        con = json.loads(response.text)
        print(con)