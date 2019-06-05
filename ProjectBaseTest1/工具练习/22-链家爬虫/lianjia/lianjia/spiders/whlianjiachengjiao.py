# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import WhlianjiachengjiaoSpiderItem

class WhlianjiachengjiaoSpider(scrapy.Spider):
    name = 'whlianjiachengjiao'
    allowed_domains = ['https://wh.lianjia.com/chengjiao/']
    start_urls = ['https://wh.lianjia.com/chengjiao/']

    # condition_area=['jiangan','jianghan','qiaokou','dongxihu','wuchang','qingshan','hongshan','hanyang','donghugaoxin','jiangxia','caidian','huangbei','xinzhou','zhuankoukaifaqu']
    condition_area=['jiangan']

    # 该方法必须返回一个可迭代对象(iterable)
    # 该对象包含了spider用于爬取的第一个Request
    def start_requests(self):
        urls=[]
        for area in self.condition_area:
            urls.append(self.start_urls[0]+area+'/')
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):     
        for info_item in response.css('.listContent>li'):
            # item=WhlianjiachengjiaoSpiderItem()
            # item['name']=info_item.xpath('./div/div[1]/a/test()').extract() 
            yield {
                'name':info_item.xpath('./div/div[1]/a/text()').extract_first()
            }
        
        next_page_url=response.css('div.page-box.house-lst-page-box>a:last-child').extract_first()
        print('下一页地址：%s'%str(next_page_url))  

    def parse_item(self,reponse):
        pass
