#coding=utf-8
from pymongo import *

#1.获得客户端，建立连接
mongoClient=MongoClient("mongodb://test:test@127.0.0.1:27017/test")

#切换数据库
db=mongoClient.test

#获取集合
users=db.user

#新增操作
# u1_ObjectID=users.insert_one({'name':'小明','gender':True,'age':21})

# print(str(u1_ObjectID))

#修改操作
# users.update_one({'name':'张三'},{'$set':{'name':'大张三'}})

#删除操作
# users.delete_one({'name':'小明'})

#查询
# cursorResult=users.find({'gender':True})  #返回cursor对象
# for cur in cursorResult:
#     print(cur['name'])

cursorResult2=users.find({'age':{'$gt':23}}).sort('_id',1).skip(1).limit(3)
for cur in cursorResult2:
    print(cur['name'])

