#-*-coding:utf-8-*-

from MySqlHelper import MySqlHelper
from RedisHelper import RedisHelper
from hashlib import sha1


def main():
    """用户登录"""
    name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if name=='':
        print('用户名不正确')
        return
    if pwd=='':
        print('密码不正确')
        return
    checkUser(name,pwd)


def checkUser(name,password):
    '''检查登录用户信息'''
    red=RedisHelper('127.0.0.1',6379,'123456')
    #验证redis里面是否存有数据
    if red.get(name)==None:
        #从mysql数据库取数
        mysqlHelper=MySqlHelper('localhost',3306,'root','root','test')
        sql='select * from user where UserName=%s';        
        params=[name]
        result=mysqlHelper.get_one(sql,params)
        if result==None:
            print('用户名错误')
        else:
            #存入redis里面
            red.set(name,result[5])

            sha1Str=strToSha1(password)
            if sha1Str!=result[5]:
                print('密码错误')
            else:
                print('登录成功')
    else:
        sha1Str=strToSha1(password)
        if sha1Str!=str(red.get(name)):
            print('密码错误')
        else:
            print('登录成功')


def strToSha1(orgStr):
    '''字符串sha1加密'''
    sha1Str=None
    try:
        s1=sha1()
        s1.update(orgStr.encode())
        sha1Str=s1.hexdigest()
    except Exception as ex:
        print(ex)
    return sha1Str
    

if __name__ == '__main__':
    main()
