#coding=utf-8

from MySqlHelper import MySqlHelper 
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
    mysqlHelper=MySqlHelper('localhost',3306,'root','root','test')
    sql='select * from user where UserName=%s';
    params=[name]
    result=mysqlHelper.get_one(sql,params)
    if result==None:
        print('用户名错误')
    else:
        sha1Str=strToSha1(password)
        if sha1Str!=result[5]:
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