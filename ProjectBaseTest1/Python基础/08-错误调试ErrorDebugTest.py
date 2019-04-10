# -*- coding: utf-8 -*-
import logging
import pdb
import re
logging.basicConfig(level=logging.INFO)
#调试
# def foo(s):
#     n=int(s)
#     print('>>>n=%s'%n)
#     return 10/n
# def main():
#     foo('0')
# main()

# 断言 assert
# 凡是可以用 print() 来辅助查看的地方，都可以用断言 assert 来替代
# 判断条件为True ，则正常，继续执行，否则为 False,后面的代码就会报错
# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zero!'
#     return 10/n
# def main():
#     foo('0')
# main()

# logging
# 允许指定记录信息的级别，有 debug info warning error几个级别
# s='0'
# n=int(s)
# logging.info('n=%d'%n)
# print(10/n)

# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('0')
#     except Exception as ex:
#         logging.exception(ex)
# main()
# print('end')


# pdb
# 让程序单步方式运行，可以随时查看运行状态。
#pdb python -m pdb ErrorDebugTest.py
# s='0'
# n=int(s)
# print(10/n)


# pdb.set_trace()
# 设置断点
# s='0'
# n=int(s)
# pdb.set_trace()
# print(10/n)

#单元测试
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value


#文档测试
# m=re.search('(?<=abc)def', 'abcdef')
# print(m.group(0))

def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n>=0 else (-n)

    