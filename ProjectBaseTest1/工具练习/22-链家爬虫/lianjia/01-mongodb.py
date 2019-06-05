# -*- coding: utf-8 -*-

from pymongo import *

#1.获得客户端，建立连接
host="127.0.0.1"
port =27017
dbname = "spider_data"
sheetname = "whlianjiachengjiao"
# 创建 MongoDB 数据库连接
client=MongoClient("mongodb://%s:%s@%s:%s/%s"%('spider_data','spider_data',host,port,dbname))
db=client[dbname]
whlianjiachengjiao=db[sheetname]



u1_ObjectID=whlianjiachengjiao.insert_one({'name':'小明','gender':True,'age':21})

print(str(u1_ObjectID))