# -*- coding: utf-8 -*-
import re

import scrapy
from wxapp.items import WxappItem

class TestOneSpider(scrapy.Spider):
    name = 'test_one'  # 爬虫名字
    allowed_domains = ['search.51job.com']  # 允许爬取的域名
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    def parse(self, response):
        cons = response.xpath("//div[@class='el']")
        print('=' * 40)
        print(cons[4].get())
        for con in cons[4:]:
            name = con.xpath(".//span[@class='t2']/a/@title").get()
            work = con.xpath(".//p/span/a/@title").get()
            place = con.xpath(".//span[@class='t3']/text()").get()
            salary = con.xpath(".//span[@class='t4']/text()").get()
            time = con.xpath(".//span[@class='t5']/text()").get()
            # print('='*40)
            # print(name)
            # print(work)
            # print(place)
            # print(salary)
            # print(time)
            # print('=' * 40)
            # data_dict = {
            #     'name': name,
            #     'work': work,
            #     'place': place,
            #     'salary': salary,
            #     'time': time
            # }
            item = WxappItem(name=name, work=work, place=place, salary=salary, time=time)
            yield item

        next_url = response.xpath('//div[@class="dw_page"]//li[last()]/a/@href').get()
        print(next_url)
        page = re.match('.*python,2,(.*?).html', next_url)
        # print(a.group(1))

        if int(page.group(1)) > 200:
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)
