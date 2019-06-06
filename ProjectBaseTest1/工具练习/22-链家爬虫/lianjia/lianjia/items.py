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

# 已经成交的二手房
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

# 正在销售的二手房
class WhlianjiaershoufangSpiderItem(scrapy.Item):
    url=scrapy.Field()  # 详细url
    title = scrapy.Field() # 标题
    onPrice=scrapy.Field() # 售价
    unitPrice=scrapy.Field() # 单价
    communityName=scrapy.Field() # 小区名称
    houseType=scrapy.Field() # 房屋类型
    houseSize=scrapy.Field() # 房屋面积
    houseDirection=scrapy.Field() # 房屋朝向
    houseDecoration=scrapy.Field() # 装修情况
    houseFlood=scrapy.Field() # 楼层 年代
    housePosition=scrapy.Field() # 小区 位置
    onDate=scrapy.Field() # 发布日期
    visit=scrapy.Field() # 带看次数
    
    


