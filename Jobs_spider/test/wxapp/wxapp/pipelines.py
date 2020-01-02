# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

from pandas import DataFrame, Series
import pandas as pd

# class WxappPipeline(object):
#
#     def open_spider(self, spider):
#         self.fp = open('data.json', 'w')
#         # print('开始--------')
#
#     def process_item(self, item, spider):
#         self.fp.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         # print('结束--------')


# from scrapy.exporters import JsonItemExporter
#
# class WxappPipeline(object):
#
#     def open_spider(self, spider):
#         self.fp = open('data.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False)
#         self.exporter.start_exporting()
#         # print('开始--------')
#
#     def process_item(self, item, spider):
#         # self.fp.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         # print('结束--------')

from scrapy.exporters import JsonLinesItemExporter
# from scrapy.pipelines.images import ImagesPipeline


class WxappPipeline(object):

    def open_spider(self, spider):
        self.fp = open('data.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
        # self.exporter.start_exporting()
        # print('开始--------')

    def process_item(self, item, spider):
        # self.fp.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
        self.exporter.export_item(item)
        # print('查看item是不是字典', item)
        s = Series(eval(item.__str__()))
        # print(s)
        df = DataFrame()
        df = df.append(s, ignore_index=True)
        if not os.path.exists('test.csv'):
            df.to_csv('test.csv', mode='a', header=1)
        else:
            df.to_csv('test.csv', mode='a', header=0)
        return item

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        self.fp.close()
        # print('结束--------')



# class MyImagesPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         requests = super().get_media_requests(item, info)
#         for request in requests:
#             request.item = item
#         return requests
#
#     def file_path(self, request, response=None, info=None):