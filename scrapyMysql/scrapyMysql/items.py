# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapymysqlItem(scrapy.Item):

    tag = scrapy.Field() # 标签字段
    cont = scrapy.Field() # 名言内容

