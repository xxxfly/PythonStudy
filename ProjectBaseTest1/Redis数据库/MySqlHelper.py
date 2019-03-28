#coding=utf-8

from pymysql import *


#封装
class MySqlHelper(object):
    '''MySql帮助类'''
    def __init__(self,host,port,username,passwd,database,charset='utf8'):
        '''初始化数据库连接参数'''
        self.host=host
        self.port=port
        self.username=username
        self.passwd=passwd
        self.database=database
        self.charset=charset

    def open(self):
        '''建立数据库连接'''
        self.conn=connect(host=self.host,port=self.port,user=self.username,password=self.passwd,database=self.database,charset=self.charset)
        self.cursor=self.conn.cursor()

    def close(self):
        '''关闭数据库连接'''
        self.cursor.close()
        self.conn.close()

    def cud(self,sql,params=()):
        ''''基本新增、修改、删除操作'''
        count=0
        try:
            self.open()
            count=self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception as ex:
            print(ex)
        return count

    def get_one(self,sql,params=()):
        '''查询单条记录操作'''
        result=None
        try:
            self.open()
            self.cursor.execute(sql,params)
            result=self.cursor.fetchone()
            self.close()
        except Exception as ex:
            print(ex)
        return result

    def get_all(self,sql,params=()):
        '''查询多条记录操作'''
        list=()
        try:
            self.open()
            self.cursor.execute(sql,params)
            list=self.cursor.fetchall()
            self.close()            
        except Exception as ex:
            print(ex)
        return list