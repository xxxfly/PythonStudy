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

# 武汉已经成交的二手房
class WhlianjiachengjiaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    url=scrapy.Field()
    title = scrapy.Field() # 标题
    dealPrice=scrapy.Field() # 成交价格
    unitPrice=scrapy.Field() # 单价
    dealDate=scrapy.Field() # 成交日期
    onPrice=scrapy.Field() # 挂牌价格    
    communityName=scrapy.Field() # 小区名称
    houseType=scrapy.Field() # 房屋类型
    houseSize=scrapy.Field() # 房屋面积
    houseDirection=scrapy.Field() # 房屋朝向
    houseDecoration=scrapy.Field() # 装修情况
    houseFlood=scrapy.Field() # 楼层 年代  
    dealCycleDay=scrapy.Field() # 挂牌周期
    houseArea=scrapy.Field() # 小区 区域

# 武汉正在销售的二手房
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
    houseArea=scrapy.Field() # 小区 区域
    onDate=scrapy.Field() # 发布日期
    visit=scrapy.Field() # 带看次数
    

# 杭州已经成交的二手房
class HzlianjiachengjiaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    url=scrapy.Field()
    title = scrapy.Field() # 标题
    dealPrice=scrapy.Field() # 成交价格
    unitPrice=scrapy.Field() # 单价
    dealDate=scrapy.Field() # 成交日期
    onPrice=scrapy.Field() # 挂牌价格    
    communityName=scrapy.Field() # 小区名称
    houseType=scrapy.Field() # 房屋类型
    houseSize=scrapy.Field() # 房屋面积
    houseDirection=scrapy.Field() # 房屋朝向
    houseDecoration=scrapy.Field() # 装修情况
    houseFlood=scrapy.Field() # 楼层 年代  
    dealCycleDay=scrapy.Field() # 挂牌周期
    houseArea=scrapy.Field() # 小区 区域

# 杭州正在销售的二手房
class HzlianjiaershoufangSpiderItem(scrapy.Item):
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
    houseArea=scrapy.Field() # 小区 区域
    onDate=scrapy.Field() # 发布日期
    visit=scrapy.Field() # 带看次数
    


