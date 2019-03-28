#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import time

# #创建一个socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# s.connect(('www.sina.com.cn',80))

# #发送数据：
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# #接收数据
# buffer=[]
# while True:
#     #每次最多接收1kb字节
#     d=s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data=b''.join(buffer)

# #关闭连接
# s.close()


# #解析data
# header,html=data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# #把接收的数据写入文件
# with open('File/sina.html','wb') as f:
#     f.write(html)


# #客户端
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# s.connect(('127.0.0.1',9999))
# #接收欢迎消息
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael',b'Tracy',b'Sarah']:
#     #发送数据
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()




#UDP
#客户端
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarch']:
    #发送数据
    s.sendto(data,('127.0.0.1',9999))
    #接收数据   
    print(s.recv(1024).decode('utf-8'))
s.close() 

