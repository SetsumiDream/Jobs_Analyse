# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.exporters import JsonLinesItemExporter
from pandas import DataFrame, Series


class SpiderBossjobPipeline(object):
    def open_spider(self, spider):
        self.fp = open('data.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        s = Series(eval(item.__str__()))
        df = DataFrame()
        df = df.append(s, ignore_index=True)
        if not os.path.exists('test.csv'):
            df.to_csv('test.csv', mode='a', header=1)
        else:
            df.to_csv('test.csv', mode='a', header=0)
        return item

    def close_spider(self, spider):
        self.fp.close()