# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpSpItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()
    # define the fields for your item here like:






