# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TestRegularSpider(CrawlSpider):
    name = 'test_regular'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    rules = (
        # Rule(LinkExtractor(allow=r'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,\d.html.+lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='), follow=True),
        Rule(LinkExtractor(allow=r'https://jobs.51job.com/\w+-\w+/\d+\.html.+'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):

        work = response.xpath('//div[@class="in"][1]//h1/@title').get()
        company = response.xpath('//div[@class="in"][1]//p[@class="cname"]/a[1]/@title').get()
        print(work, company)


