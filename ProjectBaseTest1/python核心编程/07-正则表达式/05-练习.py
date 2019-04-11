# coding=utf-8

import re


def test1():
    """
    匹配网站
    """
    print(re.sub(r'http://.+?/','','http://www.interoem.com/messageinfo.asp?id=35'))
    print(re.sub(r'(http://.+?/).*',lambda x:x.group(1),'http://www.interoem.com/messageinfo.asp?id=35'))
    print(re.sub(r'(http://.+?/).*',lambda x:x.group(1),'http://3995503.com/class/class09/news_show.asp?id=14'))

def test2():
    """
    查找所有单词
    """
    print(re.split(r' +','hello world ha ha'))
    print(re.findall(r'\b[a-zA-Z]+\b','hello world ha ha'))




def main():
    test2()

if __name__ == '__main__':
    main()