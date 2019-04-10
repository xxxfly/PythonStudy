#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#导入SQLLite驱动
import sqlite3
import mysql.connector
from datetime import datetime
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLLite
# #连接到SQLLite数据库
# #数据库文件是test.db
# #如果文件不存在，会自动在当前目录创建
# con=sqlite3.connect('DB/test1.db')
# #创建一个Cursor
# cursor=con.cursor()
# #执行一条SQL语句，创建USER表
# cursor.execute('create table user (id varchar(20) primary key,name varchar(40))')
# #继续执行一条SQL语句，插入一条记录
# cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
# #通过rowcount获得插入的行数
# print(cursor.rowcount)
# #关闭Cursor
# cursor.close()
# #提交事务
# con.commit()
# #关闭Connection
# con.close()


# #SQLLite
# #创建连接
# con=sqlite3.connect('DB/test1.db')
# #创建游标Cursor
# cursor=con.cursor()
# #执行sql语句
# # cursor.execute('insert into user (id,name) values (\'2\',\'Bob\')')
# #执行查询语句
# cursor.execute('select * from user where id=?',('2',))
# #获得查询结果集
# values=cursor.fetchall()
# print(values)
# cursor.close()
# # con.commit()
# con.close()


# #MySQL
# #创建连接
# conn=mysql.connector.connect(user='root',password='root',database='test')
# cursor=conn.cursor()
# #插入一行记录
# cursor.execute('INSERT INTO USER (UserID,UserName,NickName,CellPhone,PASSWORD,Email,CreateTime,UpdateTime)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',['10002','zx','郑翔','13812345678','123456','123@qq.com',datetime.now().strftime('%Y-%m-%d %H:%M:%S'),datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
# print(cursor.rowcount)

# #提交事务
# conn.commit()
# cursor.close()
# conn.close()

# #进行查询
# cursor.execute('select * from user where UserID=%s',('10001',))
# values=cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()


#创建对象的基类
Base=declarative_base()

#定义User类
class User(Base):
    #表的名字
    __tablename__='user'
    #表的结构
    ID=Column(String(11),primary_key=True)
    UserID=Column(String(256))
    UserName=Column(String(256))
    NickName=Column(String(256))
    CellPhone=Column(String(256))
    Password=Column(String(256))
    Email=Column(String(256))
    CreateTime=Column(String(256))
    UpdateTime=Column(String(256))

#初始化数据库连接
engine=create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')

#创建DBSession类型：
DBSession=sessionmaker(bind=engine)

#创建session对象
session=DBSession()

# #新增操作
# new_user=User()
# new_user.UserID='1004'
# new_user.UserName='zx'
# new_user.NickName='郑翔'
# new_user.CellPhone='123456789'
# new_user.Password='123'
# new_user.Email='111'
# new_user.CreateTime='2018-04-12 16:57:30'
# new_user.UpdateTime='2018-04-12 16:57:30'

# #添加到session
# session.add(new_user)
# #提交即保存到数据库
# session.commit()
# #关闭session
# session.close()

#查询操作
#创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user=session.query(User).filter(User.UserID=='10002').one() 
#打印类型和对象属性
print('type:',type(user))
print('UserID:',user.UserID)
print('NickName:',user.NickName)
print('CreateTime:',user.CreateTime)
#关闭Session
session.close()


