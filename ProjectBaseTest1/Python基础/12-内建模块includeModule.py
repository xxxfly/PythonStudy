# -*- coding: utf-8 -*-
from datetime import datetime,timedelta,timezone
import time

#datetime
#获取当前日期
# now=datetime.now()
# print(now)
# print(type(now))

#获取指定日期
# dt=datetime(2017,2,27,12,20,50)
# print(dt)

#datetime转换为timestamp
# timestamp=0=1970-1-1 00:00:00 UTC+0:00 
# timestamp=0=1970-1-1 08:00:00 UTC+8:00
# dt=datetime(2017,2,27,12,20,50)
# now=datetime.now()
# print(dt.timestamp())
# print(now.timestamp())

#timestamp转换为datetime
# t=1488169250.0
# print(datetime.fromtimestamp(t)) #本地时间
# print(datetime.utcfromtimestamp(t)) #UTC时间


#str转换为datetime
# cday=datetime.strptime('2018-03-28 19:36:50','%Y-%m-%d %H:%M:%S')
# print(cday)

#datetime转换str
# now=datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# print(now.strftime('%a,%b %d %H:%M'))

#datetime加减
# now=datetime.now()
# print(now)
# now=now+timedelta(hours=10)
# print(now)
# now=now-timedelta(days=1)
# print(now)
# now=now+timedelta(days=2,hours=12)
# print(now)

#本地时间转换为UTC时间
# tz_utc_8=timezone(timedelta(hours=8)) #创建时区UTC+8：00
# now=datetime.now()
# print(now)
# dt=now.replace(tzinfo=tz_utc_8) #强制设置为UTC+8:00
# print(dt)

#时区转换
#拿到UTC时间，并强制设置时区为UTC+0:00
# utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# #astimezone()将转换时区为北京时间：
# bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# #astimezone()将转换时区为东京时间：
# tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# #astimezone()将北京时间转换为东京时间
# tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)


from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

#collections
#namedtuple
# Point=namedtuple('Point',['x','y'])
# p=Point(1,2)
# print(p.x)
# print(p.y)
# print(isinstance(p,Point))
# print(isinstance(p,tuple))


#deque
# q=deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)


#defaultdict
# dd=defaultdict(lambda:'N/A')
# dd['key1']='abc'
# print(dd['key1'])
# print(dd['key2'])


#OrderedDict
# dd=dict([('a',1),('b',2),('c',3)])
# print(dd) #dict的Key是无序的
# od=OrderedDict([('a',1),('b',2),('c',3)])
# print(od) #OrderedDict的Key是有序的

# od1=OrderedDict()
# od1['z']=1
# od1['y']=1
# od1['x']=1
# print(list(od1.keys()))

#Counter
# c=Counter()
# for ch in 'Programming':
#     c[ch]=c[ch]+1
# print(c)


import base64

#base64
# b64en=base64.b64encode(b'binary\x00string')
# print(b64en)
# b64de=base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
# print(b64de)

# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64decode(b'abcd--__'))
# def safe_base64_decode(s):
#     if len(s)%4!=0:
#         s=s+b'='*(4-len(s)%4)
#     return base64.urlsafe_b64decode(s)
# print(safe_base64_decode(b'YmluYXJ5AHN0cmluZw'))


import struct

#struct
# n=10240099
# b1=(n & 0xff000000) >> 24
# print(b1)
# b2=(n & 0xff0000) >> 16
# print(b2)
# b3= (n & 0xff00) >> 8
# print(b3)
# b4=n&0xff
# print(b4)
# bs = bytes([b1, b2, b3, b4])
# print(bs)

# structI=struct.pack('>I',10240099)
# print(structI)

# structIH1=struct.unpack('>I',b'\x00\x9c@c')
# print(structIH1)

# structIH2=struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
# print(structIH2)

#操作图片
# try:
#     f=open('File/test.png','rb')
#     pngBytes=f.read()
#     print(struct.unpack('<ccIIIIIIHH',pngBytes[:30]))
# finally:
#     f.close()


import hashlib

#hashlib 摘要算法
# md5=hashlib.md5()
# # md5.update('how to use md5 in pyhton hashlib?'.encode('utf-8'))
# # print(md5.hexdigest())

# md5.update('how to use md5 in'.encode('utf-8'))
# md5.update(' pyhton hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# sha1=hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())


import hmac
# hmac
# 通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
# message=b'Hello,world'
# key=b'secret'
# h=hmac.new(key,message,digestmod='MD5')
# print(h.hexdigest())


import itertools
# itertools
# 用于操作迭代对象的函数
# count() 会创建一个无限循环的迭代器
# nutuals=itertools.count(1)
# for n in nutuals:
#     time.sleep(1)
#     print(n)

# cycle() 会把传入的一个序列无限循环下去
# cs=itertools.cycle('ABC')
# for n in cs:
#     time.sleep(1)
#     print(n)

# repeat() 把一个元素无限重复下去，第二个参数可以限定重复次数
# ns=itertools.repeat('AB',3)
# for n in ns:
#     time.sleep(1)
#     print(n)


# takewhile() 函数根据条件判断来截取一个有序的序列
# natuals=itertools.count(1)
# ns=itertools.takewhile(lambda x:x<=10,natuals)
# print(list(ns))

# chain() 把一组迭代对象串联起来，形成一个更大的迭代器。
# for c in itertools.chain('AB','CD'):
#     time.sleep(1)
#     print(c)

# groupby() 把迭代器中相邻的重复元素挑出来放在一起
# for key,group in itertools.groupby('AAABCCCAABB'):
#     print(key,list(group))

# for key,group in itertools.groupby('AaaBbCaAa',lambda x:x.upper()):
#     print(key,list(group))


from contextlib import contextmanager

# 读写资源完毕之后，要关闭它们
# try:
#     f=open('File/test01.txt','r',encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# width 语句可以方便的使用资源，不必担心资源没有关闭
# with open('File/test01.txt','r',encoding='utf-8') as f:
#     print(f.read())

# 任何对象，只有正确实现了上下文管理，就可以使用 width 语句。
# 实现上下文是用过 __enter__ 和 __exit__ 两个方法实现的
# class Query(object):
#     def __init__(self,name):
#         self.name=name
#     def __enter__(self):
#         print('Begin')
#         return self
#     def __exit__(self,exc_type,exc_value,trackback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#     def query(self):
#         print('Query info about %s'%self.name)
# with Query('Bob') as q:
#     q.query()



# python 提供了更简答的写法
# class Query(object):
#     def __init__(self,name):
#         self.name=name
#     def query(self):
#         print('Query info about %s...'%self.name)

# @contextmanager
# def create_query(name):
#     print('Begin')
#     q=Query(name)
#     yield q
#     print('End')

# with create_query('Bob') as q:
#     q.query()


#	1. with语句首先执行yield之前的语句，因此打印出<h1>；
#	2. yield调用会执行with语句内部的所有语句，因此打印出hello和world；
#	3. 最后执行yield之后的语句，打印出</h1>。
# @contextmanager
# def tag(name):
#     print('<%s>'%name)
#     yield
#     print('</%s>'%name)
# with tag('h1'):
#     print('Hello')
#     print('world')


from contextlib import closing

#closing
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)


from urllib import request,parse
import urllib

#urllib-Get
# with request.urlopen('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv988&productId=1024728&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1') as r:
#     data=r.read()
#     print('Status',r.status,r.reason)
#     for k,v in r.getheaders():
#         print('%s:%s' % (k,v))
#     print('Date:',data)

# 往 Request 对象中添加 HTTP 头部信息
# req=request.Request('https://jd.com')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as r:
#     print('Status',r.status,r.reason)
#     for k,v in r.getheaders():
#         print('%s:%ss'%(k,v))
#     print('Data')

#urllib-Post
# print('test post request...')
# key='www.holyblade.com'
# ADAccount=input('ADAccount：')
# EPGName=input('EPGName：')
# timestamp=str(datetime.now().timestamp())[:10]
# md5=hashlib.md5()
# md5.update(ADAccount.encode('utf-8'))
# md5.update(timestamp.encode('utf-8'))
# md5.update(key.encode('utf-8'))
# sign=md5.hexdigest()
# # post_data=parse.urlencode([
# #     ('ADAccount',ADAccount),
# #     ('Timestamp',timestamp),
# #     ('sign',sign),
# #     ('EPGName',EPGName)
# # ])

# post_data={'ADAccount':ADAccount,'Timestamp':timestamp,'Sign':sign,'EPGName':EPGName}
# req=request.Request('http://192.168.1.32:8000/api_NewPractice/sdk/getEpgInfo.ashx')

# req.add_header('sj','sj')
# with request.urlopen(req,data=str(post_data).encode('utf-8')) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data:',f.read().decode('utf-8'))


# 代理
# proxy_handler=urllib.request.ProxyHandler({'http':'http://www.example.com:3128/'})
# proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm','host','username','password')
# opener=urllib.request.build_opener(proxy_handler,proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass



from xml.parsers.expat import ParserCreate
# 操作XML
# SAX 是流模式，边读边解析，占用内存小，解析快。
# class DefaultSaxHandler(object):
#     def start_element(self,name,attrs):
#         print('sax:start_element:%s,attrs:%s'%(name,str(attrs)))
#     def end_element(self,name):
#         print('sax:end_element:%s'%name)
#     def char_data(self,text):
#         print('sax:char_data:%s'%text)
# xml=r'''<?xml version="1.0"?>
#     <ol>
#         <li><a href="/python">Python</a></li>
#         <li><a href="/ruby">Ruby</a></li>
#     </ol>
# '''
# handler=DefaultSaxHandler()
# parse=ParserCreate()
# parse.StartElementHandler=handler.start_element
# parse.EndElementHandler=handler.end_element
# parse.CharacterDataHandler=handler.char_data
# parse.Parse(xml)



from html.parser import HTMLParser
from html.entities import name2codepoint
# HTMLParser
# 
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self,tag,attrs):
#         print('<%s>' % tag)
#     def handle_endtag(self,tag):
#         print('<%s/>' % tag)
#     def handle_startendtag(self,tag,attrs):
#         print('<%s>' % tag)
#     def handle_data(self,data):
#         print(data)
#     def handle_comment(self,data):
#         print('<!---',data,'--->')
#     def handle_entityref(self,name):
#         print('&%s:'%name)
#     def handle_charref(self,name):
#         print('&#%s:'%name)
# parser=MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!---test html parser--->
#     <p>Some <href=\"#\">html</a>HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')