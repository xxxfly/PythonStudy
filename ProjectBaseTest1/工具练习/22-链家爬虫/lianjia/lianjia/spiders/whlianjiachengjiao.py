# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import WhlianjiachengjiaoSpiderItem

class WhlianjiachengjiaoSpider(scrapy.Spider):
    name = 'whlianjiachengjiao'
    allowed_domains = []
    start_urls = ['https://wh.lianjia.com/chengjiao/']

    # condition_area=['jiangan','jianghan','qiaokou','dongxihu','wuchang','qingshan','hongshan','hanyang','donghugaoxin','jiangxia','caidian','huangbei','xinzhou','zhuankoukaifaqu']

    # 该方法必须返回一个可迭代对象(iterable)
    # 该对象包含了spider用于爬取的第一个Request
    # def start_requests(self):
    #     urls=[]
    #     for area in self.condition_area:
    #         urls.append(self.start_urls[0]+area+'/')
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):     
        # 获取各地区 条件的页面
        area_urls=[]
        for item in response.css('div[data-role="ershoufang"] a::attr(href)').extract():
            url=self.start_urls[0]+item.replace('/chengjiao/','')
            area_urls.append(url)
        for url in area_urls:
            yield scrapy.Request(url,callback=self.parse_loop)
        
    def parse_loop(self,response):
        url=response.url
        for i in range(1,101):
            new_url=url+'pg'+str(i)+"/"
            yield scrapy.Request(new_url,callback=self.parse_item)
        
    def parse_item(self,response):
        for info_item in response.css('.listContent>li'):
            item=WhlianjiachengjiaoSpiderItem()
            item['url']=response.url
            item['name']=info_item.css('div.title>a::text').extract_first()
            item['totalPrice']=info_item.css('div.totalPrice>span.number::text').extract_first()
            item['houseInfo']=info_item.css('div.houseInfo::text').extract_first()
            item['dealDate']=info_item.css('div.dealDate::text').extract_first()
            item['positionInfo']=info_item.css('div.positionInfo::text').extract_first()
            item['dealHouseInfo']=info_item.css('div.dealHouseInfo>span.dealHouseTxt>span::text').extract_first()
            item['dealCycleeInfo']=info_item.css('div.dealCycleeInfo>span.dealCycleTxt>span:nth-child(2)::text').extract_first()
            item['onPrice']=info_item.css('div.dealCycleeInfo>span.dealCycleTxt>span:nth-child(1)::text').extract_first()

            yield item
