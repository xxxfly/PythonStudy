# -*- coding: utf-8 -*-

from pymongo import *
from MySqldbHepler import MySqlHelper




class MongoDBHelper(object):
    """
    MongoDB 类
    """
    def __init__(self,host,port,dbname,username,pwd):
        """
        获得客户端，建立连接
        """
        self.host=host
        self.port =port
        self.dbname = dbname
        self.username=username
        self.pwd=pwd
        
    def mgClient(self):
        """
        创建 MongoDB 数据库连接
        """
        self.client=MongoClient("mongodb://%s:%s@%s:%s/%s"%(self.username,self.pwd,self.host,self.port,self.dbname))
    
    def mgCollection(self,sheetname):    
        """
        获取表对象
        """  
        try:
            self.mgClient()  
            db=self.client[self.dbname]
            self.col=db[sheetname]
        except Exception as ex:
            print('获取集合出错:'+ex)
        
    
    def getAllbyPage(self,sheetname,page_size,page_index):
        """
        获取分页数据
        @sheetname 集合名称
        @page_size 分页大小
        @page_index 当前页码
        """
        cursor_result=None
        try:
            self.mgCollection(sheetname)
            cursor_result=self.col.find({}).skip(page_size*(page_index-1)).limit(page_size)            
        except Exception as ex:
            print('获取分页数据出错:'+ex)
        return cursor_result
    
    def getCount(self,sheetname):
        """
        获取总数量
        """
        count=0
        try:
            self.mgCollection(sheetname)
            count=self.col.count({})
        except Exception as ex:
            print('获取分页数据出错:'+ex)
        return count
        


def copyChenJiaoData():    
    mongo=MongoDBHelper('127.0.0.1',27017,'spider_data','spider_data','spider_data')
    params=[]
    mysql=MySqlHelper('127.0.0.1',3306,'spider_data','spider_data','spider_data')
    
    totalCount=mongo.getCount('whlianjiachengjiao')
    
    page_size=100
    page_index=1
    page_number=totalCount//page_size+1
    
    for i in range(2,page_number+1):
        result=mongo.getAllbyPage('whlianjiachengjiao',page_size,i)
        for item in result:
            print('-url:%s'%(item['url']))
            try:
                param=((item['url'],item['title'],item['communityName'],item['houseType'],item['houseSize'],item['dealPrice'],item['unitPrice'],item['dealDate'],item['onPrice'],item['dealCycleDay'],item['houseDirection'],item['houseDecoration'],item['houseFlood']))

                sql='insert into whlianjiachengjiao(url,title,communityName,houseType,houseSize,dealPrice,unitPrice,dealDate,onPrice,dealCycleDay,houseDirection,houseDecoration,houseFlood) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

                cur_count=mysql.cud(sql,param)

            except Exception as ex:
                print('---出错---:%s'%(item['url']))
                print(ex)
                # 记录错误文件
                with open('error.txt','a',encoding='utf-8') as f:
                    f.write(item['url']+'\r\n')               
            # params.append(param)

    

if __name__ == '__main__':
    copyChenJiaoData()
 
