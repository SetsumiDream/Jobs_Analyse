# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class TestRegularSpider(CrawlSpider):
    name = 'test_regular'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    rules = (
        Rule(LinkExtractor(allow=r'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,\d+.html.+lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='), follow=True),
        Rule(LinkExtractor(allow=r'https://jobs.51job.com/\w+-\w+/\d+\.html.+'), callback='parse_detail', follow=False),
        Rule(LinkExtractor(allow=r'https://jobs.51job.com/\w+/\d+\.html.+'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):

        workname = response.xpath('//div[@class="in"]//h1/@title').get()
        salary = response.xpath('//div[@class="in"]//div[@class="cn"]//strong/text()').get()
        company = response.xpath('//div[@class="in"]//p[@class="cname"]/a[1]/@title').get()
        cptype = response.xpath('//div[@class="com_tag"]//p[@class="at"]/@title').get()
        business = response.xpath('//div[@class="com_tag"]//a/text()').getall()
        msg = response.xpath('//div[@class="in"]//p[@class="msg ltype"]/@title').get().split('  |  ')
        if len(msg) == 4:
            msg.insert(2, None)
        place, exp, edu, needNum, time = msg[0], msg[1], msg[2], msg[3], msg[4]
        msg1 = response.xpath('//div[@class="tBorderTop_box"][1]//p/text()').getall()
        work_msg = ''.join(''.join(msg1).split())

        item = WxappItem(workname=workname, salary=salary, company=company, cptype=cptype, business=business, place=place, exp=exp, edu=edu, needNum=needNum, time=time, work_msg=work_msg)
        yield item
        # print(workname, company, cptype, business, place, exp, edu, needNum, time, work_msg)


