#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import time

# #服务器
##TCP
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# #监听端口
# s.bind(('127.0.0.1',9999))

# #开始监听
# s.listen(5)
# print('Waiting for connection...')

# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
    
# #接收连接
# while True:
#     #接受一个新连接
#     sock,addr=s.accept()
#     #创建新线程来处理TCP连接
#     t=threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()


#服务端
#UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999...')
while True:
    #接收数据
    data,addr=s.recvfrom(1024)
    print('Received from %s:%s'%addr)
    s.sendto(b'Hello,%s'%data,addr)
