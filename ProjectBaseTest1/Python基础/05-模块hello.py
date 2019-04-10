# -*- coding: utf-8 -*-

# print('hrllo,world')
#print('the quick brown fox','jumps over','the lazy dog')
# print(30000)
# print('100+200=',100+200)
# name=input('请输入您的名字：')
# print('name is:',name)
'a test module'
__author__='zx'
import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,world')
    elif len(args)==2:
        print('Hello,%s'%args[1])
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'Hello,%s'%name

def _private_2(name):
    return 'Hello,%s'%name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__=='__main__':
    # test()
    print(_private_2('zx2'))
    print(greeting('zx'))

# class Hello(object):
#     def hello(self,name='world'):
#         print('hello,%s'%name)



