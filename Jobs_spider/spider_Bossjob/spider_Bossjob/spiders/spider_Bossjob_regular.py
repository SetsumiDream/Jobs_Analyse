# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from spider_Bossjob.items import SpiderBossjobItem


class SpiderBossjobRegularSpider(CrawlSpider):
    name = 'spider_Bossjob_regular'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280600-p100109/?ka=search_100109']

    rules = (
        Rule(LinkExtractor(allow=r'.+-p100109/.+'), follow=True),
        Rule(LinkExtractor(allow=r'.+/job_detail/.+'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        workname = response.xpath('//div[@class="name"]//h1/text()').get()
        salary = response.xpath('//div[@class="name"]//span[@class="salary"]/text()').get()
        company = response.xpath('//div[@class="job-sec"]//div[@class="name"]/text()').get()
        cptype = response.xpath('//div[@class="job-sec"]//li[@class="company-type"]/text()').get()
        business = response.xpath('//div[@class="job-sider"]//a[@ka="job-detail-brandindustry"]/text()').getall()
        msg = response.xpath('//div[@class="info-primary"]//p/text()').getall()[:3]
        place, exp, edu = msg[0], msg[1], msg[2]
        time = response.xpath('//div[@class="job-status"]/text()').get()
        msg1 = response.xpath('//div[@class="job-sec"]//div[@class="text"]/text()').getall()
        work_msg = ''.join(''.join(msg1).split())

        item = SpiderBossjobItem(workname=workname, salary=salary, company=company, cptype=cptype, business=business, place=place, exp=exp, edu=edu, time=time, work_msg=work_msg)
        yield item
        # print(workname, company, salary, cptype, business, place, exp, edu, time, work_msg)
        # print(workname, company, salary, cptype, business, msg, time, work_msg)

