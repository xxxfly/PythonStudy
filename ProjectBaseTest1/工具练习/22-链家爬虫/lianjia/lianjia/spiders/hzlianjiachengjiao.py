# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import HzlianjiachengjiaoSpiderItem
import re


class HzlianjiachengjiaoSpider(scrapy.Spider):
    name = 'hzlianjiachengjiao'
    allowed_domains = []
    start_urls = ['https://hz.lianjia.com/chengjiao/']

    # 地区条件
    condition_area=['xihu','xiacheng','gongshu','shangcheng','binjiang','yuhang','xiaoshan','tonglu1','chunan1','jiande','fuyang','linan','dajiangdong1','qiantangxinqu']

    # 价格条件
    condition_price=['p1','p2','p3','p4','p5','p6']

    # 该方法必须返回一个可迭代对象(iterable)
    # 该对象包含了spider用于爬取的第一个Request
    def start_requests(self):
        for area in self.condition_area:
            req_url=self.start_urls[0]+area+'/'
            yield scrapy.Request(url=req_url,callback=self.parse,dont_filter=True,meta={'area':area})
          
    def parse(self, response):     
        res_url=response.url
        area=response.meta['area']
        for p in self.condition_price:  # 价格范围条件
            for i in range(1,101):  # 循环页码
                req_url=res_url+'pg'+str(i)+p+'/'
                yield scrapy.Request(url=req_url,callback=self.parse_loop,dont_filter=True,meta={'area':area})
        
    def parse_loop(self,response):
        res_url=response.url
        area=response.meta['area']
        for info_item in response.css('.listContent>li'):            
            # 验证info_item 是否影藏实际价格
            totalPrice=info_item.css('div.totalPrice>span.number::text').extract_first()
            detail_url=info_item.css('a.img::attr(href)').extract_first()
            if totalPrice.find('*')>-1:
                yield scrapy.Request(url=detail_url,callback=self.parse_item,dont_filter=True,meta={'area':area})
            else:
                item=HzlianjiachengjiaoSpiderItem()
                item['url']=detail_url
                title=info_item.css('div.title>a::text').extract_first()
                item['title']=title
                item['houseArea']=area

                titleList=title.split(' ')
                if len(titleList)>2:
                    item['communityName']=titleList[0]
                    item['houseType']=titleList[1]
                    item['houseSize']=float(titleList[2].replace('平米',''))
                
                item['dealPrice']=float(info_item.css('div.totalPrice>span.number::text').extract_first())
                item['unitPrice']=float(info_item.css('div.unitPrice>span.number::text').extract_first())
                item['dealDate']=info_item.css('div.dealDate::text').extract_first().replace('.','-')

                onPrice=info_item.css('div.dealCycleeInfo>span.dealCycleTxt>span:nth-child(1)::text').extract_first()
                re_onPrice=re.findall(r'\d+',onPrice)
                if len(re_onPrice)>0:
                    item['onPrice']=float(re_onPrice[0])
                else:
                    item['onPrice']=0.0

                dealCycleDay=info_item.css('div.dealCycleeInfo>span.dealCycleTxt>span:nth-child(2)::text').extract_first()
                re_dealCycleDay=re.findall(r'\d+',dealCycleDay)
                if len(re_dealCycleDay)>0:
                    item['dealCycleDay']=int(re_dealCycleDay[0])
                else:
                    item['dealCycleDay']=0
                 
                houseInfo=info_item.css('div.houseInfo::text').extract_first()
                houseInfoList=houseInfo.split(' | ')
                if len(houseInfoList)>1:
                    item['houseDirection']=houseInfoList[0]
                    item['houseDecoration']=houseInfoList[1]
                item['houseFlood']=info_item.css('div.positionInfo::text').extract_first()

                yield item
 
        
    def parse_item(self,response):
        res_url=response.url
        area=response.meta['area']

        item=HzlianjiachengjiaoSpiderItem()
        item['url']=res_url
        item['houseArea']=area
        title=response.css('div.house-title>div.wrapper::text').extract_first()  
        item['title']=title
        titleList=title.split(' ')
        if len(titleList)>2:
            item['communityName']=titleList[0]
            item['houseType']=titleList[1]
            item['houseSize']=float(titleList[2].replace('平米',''))


        item['dealPrice']=float(response.css('span.dealTotalPrice>i::text').extract_first())
        item['unitPrice']=float(response.css('div.overview>div.info>div.price>b::text').extract_first())

        item['dealDate']=response.css('div.house-title>div.wrapper>span::text').extract_first().replace('.','-').replace('成交','').rstrip()

        item['onPrice']=float(response.css('div.overview>div.info>div.msg>span:nth-child(1)>label::text').extract_first())
        item['dealCycleDay']=int(response.css('div.overview>div.info>div.msg>span:nth-child(2)>label::text').extract_first())

        introContent=response.css('div.introContent')
        item['houseFlood']=introContent.css('ul>li:nth-child(2)::text').extract_first().rstrip()+introContent.css('ul>li:nth-child(8)::text').extract_first().rstrip()+introContent.css('ul>li:nth-child(6)::text').extract_first().rstrip()
        item['houseDirection']=introContent.css('ul>li:nth-child(7)::text').extract_first().rstrip()
        item['houseDecoration']=introContent.css('ul>li:nth-child(9)::text').extract_first().rstrip()

        yield item
