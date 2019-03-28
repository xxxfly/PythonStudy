#coding=utf-8

from pymysql import *


# def connTest():
#     try:
#         conn=connect(host='localhost',user='root',password='root',database='test',port=3306,charset='utf8')
#         cursor1=conn.cursor()

#         #sql='insert into students(name) values("李七")'
#         sql='update students set birthday="1998-06-25" where name="李七"'
#         cursor1.execute(sql)

#         conn.commit()
#         cursor1.close()
#         conn.close()
#     except Exception as ex:
#         print(ex)


#connTest()


# #sql语句参数化
# def connParam():
#     try:
#         conn=connect(host='localhost',user='root',password='root',database='test',port=3306,charset='utf8')
#         cursor1=conn.cursor()
#         new_name=input('请输入学生姓名:')
#         new_birthday=input('请输入学生出生日期:')
#         params=[new_name,new_birthday]
#         count=cursor1.execute('insert into students(name,birthday) values(%s,%s)',params)
#         print('count:'+str(count))
#         conn.commit()

#         cursor1.close()
#         conn.close()

#     except Exception as ex:
#         print(ex)

# connParam()


# #查询
# def connQuery():
#     try:
#         conn=connect(host='localhost',user='root',password='root',database='test',port=3306,charset='utf8')
#         cur=conn.cursor()
#         cur.execute('select * from students')
#         #result=cur.fetchone()
#         result=cur.fetchall()
#         print(result)

#         cur.close()
#         conn.close()

#     except Exception as ex:
#         print(ex)

# connQuery()


#封装
class MySqlHelper(object):
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

if __name__ == '__main__':
    
    MySqlHelper=MySqlHelper('localhost',3306,'root','root','test')
    # birthday_new=input('请输入学生生日:')
    # params=[birthday_new]
    # count=MySqlHelper.cud('update students set birthday=%s where id=11',params)
    # print('count=%d'%count)

    # name=input('请输入学生姓名：')
    # params=[name]
    # result=MySqlHelper.get_one('select * from students where name=%s',params)
    # print(result)

    result=MySqlHelper.get_all('select * from students')
    print(result)


