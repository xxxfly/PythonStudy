# coding=utf-8

import re

# search方法
def test1():
    """
    re.search() 匹配第一个结束
    """
    print(re.search(r'python','<html><h1>python</h1></html>'))
    print(re.search(r'python','<html><h1>python</h1><h2>python</h2></html>').group())
    print(re.search(r'python','<html><h1>python</h1></html>').group())
    

def test2():
    """
    re.findall() 匹配所有的
    """
    print(re.findall(r'python','<html><h1>python</h1><h2>python</h2></html>'))

def add(result):
    strNum=result.group()
    num=int(strNum)+10
    return str(num)

def test3():
    """
    re.sub()   将匹配到的数据进行替换
    """
    print(re.sub(r'php','python','c++ c python php cpp python php'))
    print(re.sub(r'\d+',add,'python=88,php=75'))


def test4():
    """
    re.split()  根据匹配进行切割字符串，并返回一个列表
    """
    print(re.split(r':|,','project:python,javascript,html'))

def main():
    test4()

if __name__ == '__main__':
    main()