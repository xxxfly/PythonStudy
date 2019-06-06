# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import WhlianjiaershoufangSpiderItem
import re
from datetime import datetime,timedelta


class WhlianjiaershoufangSpider(scrapy.Spider):
    name = 'whlianjiaershoufang'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://wh.lianjia.com/ershoufang/']

    # 地区条件
    condition_area=['jiangan','jianghan','qiaokou','dongxihu','wuchang','qingshan','hongshan','hanyang','donghugaoxin','jiangxia','caidian','huangbei','xinzhou','zhuankoukaifaqu']

    # 价格条件
    condition_price=['p1','p2','p3','p4','p5','p6']

    # 该方法必须返回一个可迭代对象(iterable)
    # 该对象包含了spider用于爬取的第一个Request
    def start_requests(self):
        urls=[]
        for area in self.condition_area:
            urls.append(self.start_urls[0]+area+'/')
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
   
    def parse(self, response):
        res_url=response.url
        for p in self.condition_price:
            for i in range(1,101):
                req_url=res_url+'pg'+str(i)+p+'/'
                yield scrapy.Request(url=req_url,callback=self.parse_item,dont_filter=True)
    
    def parse_item(self, response):
        print('--------------parse_item----------------')
        for info_item in response.css('.sellListContent>li'):
            item=WhlianjiaershoufangSpiderItem()
            item['url']=info_item.css('a.noresultRecommend::attr(href)').extract_first()
            item['title']=info_item.css('div.title>a::text').extract_first()
            item['onPrice']=info_item.css('div.totalPrice>span::text').extract_first()
            item['unitPrice']=info_item.css('div.unitPrice::attr(data-price)').extract_first()
            item['communityName']=info_item.css('div.houseInfo>a::text').extract_first()

            houseInfo=info_item.css('div.houseInfo::text').extract_first()
            houseInfoList=houseInfo.split(" | ")
            if len(houseInfoList)>4:
                if houseInfoList[2].find('室')>-1:
                    item['houseType']=houseInfoList[1].rstrip().lstrip()
                    item['houseSize']=houseInfoList[2].rstrip().lstrip().replace('平米','')
                    item['houseDirection']=houseInfoList[3].rstrip().lstrip()
                    item['houseDecoration']=houseInfoList[4].rstrip().lstrip()
                else:
                    item['houseType']=houseInfoList[1].rstrip().lstrip()+'-'+houseInfoList[2].rstrip().lstrip()
                    item['houseSize']=houseInfoList[3].rstrip().lstrip().replace('平米','')
                    item['houseDirection']=houseInfoList[4].rstrip().lstrip()
                    item['houseDecoration']=houseInfoList[5].rstrip().lstrip()
                
            
            item['houseFlood']=info_item.css('div.positionInfo::text').extract_first().replace(' - ','')
            item['housePosition']=info_item.css('div.positionInfo>a::text').extract_first()

            followInfo=info_item.css('div.followInfo::text').extract_first()
            followInfoList=followInfo.split(' / ')
            if len(followInfoList)>2:
                re_visit=re.findall(r'\d+',followInfoList[1])
                if len(re_visit)>0:
                    item['visit']=int(re_visit[0])
                else:
                    item['visit']=0
                
                now=datetime.now()
                re_onDate=re.findall(r'\d+',followInfoList[2])
                if len(re_onDate)>0:
                    days=int(re_onDate[0])
                    if followInfoList[2].find('天')>-1:
                        item['onDate']=(now-timedelta(days=days)).strftime('%Y-%m-%d')
                    elif followInfoList[2].find('月')>-1:
                        item['onDate']=(now-timedelta(days=days*30)).strftime('%Y-%m-%d')
                    else:
                        item['onDate']=(now-timedelta(days=3)).strftime('%Y-%m-%d')
                else:
                    item['onDate']=(now-timedelta(days=3)).strftime('%Y-%m-%d')

            yield item
