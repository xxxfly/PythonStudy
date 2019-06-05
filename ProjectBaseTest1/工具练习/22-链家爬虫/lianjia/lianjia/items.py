# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WhlianjiachengjiaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    url=scrapy.Field()
    name = scrapy.Field()
    totalPrice=scrapy.Field()
    houseInfo=scrapy.Field()
    dealDate=scrapy.Field()
    positionInfo=scrapy.Field()
    dealHouseInfo=scrapy.Field()
    dealCycleeInfo=scrapy.Field()
    onPrice=scrapy.Field()
    
    


