# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Brand(object):
    def process_item(self, item, spider):

        if item.get("brand"):
            item["brand"] = ''.join(item["brand"])
        else:
            return item

        return item