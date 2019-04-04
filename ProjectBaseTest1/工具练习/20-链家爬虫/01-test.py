#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-04-04 13:37:01
# Project: lianjiash

from pyspider.libs.base_handler import *

# 要爬的主地址
request_url="https://sh.lianjia.com/chengjiao"

class Handler(BaseHandler):
    # 对于整个爬虫项目的全局配置：所有的self.crawl()在请求的时候都会加载这个配置。
    crawl_config = {
    }
    
    # @every: 用于设置定时爬取任务：可以是minutes, 也可以设置为seconds
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl(request_url, callback=self.chengjiao_list)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):        
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
    
    # 爬取交易列表  
    # age: 主要是对任务url进行去重/过滤(根据taskid)，每一个url有唯一的一个标识taskid，age是一个以秒为单位的时间点，
    # 如果在这个时间范围内，遇到了相同的taskid，这个任务就会被丢弃
    @config(age=10 * 24 * 60 * 60)
    def chengjiao_list(self,response):
        # response.doc返回一个pyquery对象
        for each in response.doc('.listContent>li>a').items():
            self.crawl(each.attr.href,callback=self.chengjiao_detail)
        
        # 爬取下一页数据        
        next_page=response.doc('.house-lst-page-box>a:last')  
        print(next_page.text())
        if "下一页" in next_page.text():            
            self.crawl(next_page.attr.href,callback=self.chengjiao_list,validate_cert=False)
            
            
            
     
    # 交易详细
    @config(priority=2)
    def chengjiao_detail(self, response): 
        return {
            "title":response.doc('.house-title h1').text(),
            "dealDate":response.doc('.house-title span').text(),
            "totalPrice":response.doc('.dealTotalPrice').text(),
            "totalPrice":response.doc('.dealTotalPrice').text(),
            "price":response.doc('.price>b').text()+"元/平",
            "onPrice":response.doc('.msg>span:eq(0)>label').text()+"万",
            "onDate":response.doc('.msg>span:eq(1)>label').text()+"天",
            "changeNumber":response.doc('.msg>span:eq(2)>label').text()+"次",
            "visitHouse":response.doc('.msg>span:eq(3)>label').text()+"次",
            "like":response.doc('.msg>span:eq(4)>label').text()+"人",
            "visitPage":response.doc('.msg>span:eq(5)>label').text()+"次",
            "info1":response.doc('.introContent>.base>.content>ul>li:eq(0)').text(),
            "info2":response.doc('.introContent>.base>.content>ul>li:eq(1)').text(),
            "info3":response.doc('.introContent>.base>.content>ul>li:eq(2)').text(),
            "info4":response.doc('.introContent>.base>.content>ul>li:eq(3)').text(),
            "info5":response.doc('.introContent>.base>.content>ul>li:eq(4)').text(),
            "info6":response.doc('.introContent>.base>.content>ul>li:eq(5)').text(),
            "info7":response.doc('.introContent>.base>.content>ul>li:eq(6)').text(),
            "info8":response.doc('.introContent>.base>.content>ul>li:eq(7)').text(),
            "info9":response.doc('.introContent>.base>.content>ul>li:eq(8)').text(),
            "info10":response.doc('.introContent>.base>.content>ul>li:eq(9)').text(),
            "info11":response.doc('.introContent>.base>.content>ul>li:eq(10)').text(),
            "info12":response.doc('.introContent>.base>.content>ul>li:eq(11)').text(),
            "info13":response.doc('.introContent>.base>.content>ul>li:eq(12)').text(),
            "info14":response.doc('.introContent>.base>.content>ul>li:eq(13)').text(),
        }