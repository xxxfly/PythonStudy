#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from WebTest import application

#创建一个服务器，IP地址为空，端口为9999，处理函数是application
httpd=make_server('',9999,application)
print('Serving HTTP on port 9999...')
#开始监听http请求
httpd.serve_forever()
