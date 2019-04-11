# coding=utf-8

import re


# 分组匹配
def test1():
    """
    分组匹配
    |   匹配左右任意一个表达式
    (ab)    将括号中字符作为一个分组
    \num 引用分组 num 匹配到的字符串
    (?P<name>) 分组起别名
    (?P=name)   引用别名为 name 分组匹配到的字符串
    """

    print('0-100 之间的数字 '+'-'*20)
    print(re.match(r'[1-9]\d?$|0$|100$','100'))
    print(re.match(r'[1-9]\d?$|0$|100$','0'))
    print(re.match(r'[1-9]\d?$|0$|100$','78'))
    print(re.match(r'[1-9]\d?$|0$|100$','078'))
    print(re.match(r'[1-9]\d?$|0$|100$','201'))
    print(re.match(r'[1-9]?\d{1}$|100$','0'))
    print(re.match(r'[1-9]?\d{1}$|100$',''))

    url='https://docs.python.org/3.6/whatsnew/3.6.html'
    print('(ab) '+'-'*20)
    print(re.match(r'<h1>(.*)</h1>','<h1>分组匹配</h1>'))
    print(re.match(r'<h1>(.*)</h1>','<h1>分组匹配</h1>').group())
    print(re.match(r'<h1>(.*)</h1>','<h1>分组匹配</h1>').group(1))
    print(re.match(r'(<h1>).*(</h1>)','<h1>分组匹配</h1>').group(0))
    print(re.match(r'(<h1>).*(</h1>)','<h1>分组匹配</h1>').group(1))
    print(re.match(r'(<h1>).*(</h1>)','<h1>分组匹配</h1>').group(2))
    print(re.match(r'(<h1>).*(</h1>)','<h1>分组匹配</h1>').groups()[0])

    print('\num '+'-'*20)
    print(re.match(r'<.+><.+>.+</.+><.+>','<html><h1>python</h1></html>').group(0))
    print(re.match(r'<.+><.+>.+</.+><.+>','<html><h1>python</h1></h>').group(0))
    print(re.match(r'<(.+)><(.+)>.+</\2></\1>','<html><h1>python</h1></html>').group(0))
    print(re.match(r'<(.+)><(.+)>.+</\2></\1>','<html><h1>python</h1></h>'))

    print('邮箱匹配 '+'-'*20)
    print(re.match(r'(\w+)@(163|126|gmail|qq)\.(com|cn|net)$','123@qq.com'))
    print(re.match(r'(\w+)@(163|126|gmail|qq)\.(com|cn|net)$','123@qq.com').group(1))

    print('(?p<name>) '+'-'*20)
    print(re.match(r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>','<html><h1>python</h1></html>'))
    






def main():
    test1()

if __name__ == '__main__':
    main()