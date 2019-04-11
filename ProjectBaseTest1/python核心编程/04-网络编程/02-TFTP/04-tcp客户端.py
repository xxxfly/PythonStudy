#coding=utf-8
from socket import *
#tcp 传输控制协议
#upd 用户数据报协议

#tcp
#1.稳定
#2.相对udp而言慢一些
#3.web服务器都是使用tcp

#1.创建套接字
clientScoket=socket(AF_INET,SOCK_STREAM)
#链接服务器
clientScoket.connect(('192.168.108.131',8899))
#发送数据
clientScoket.send('haha'.encode('utf-8'))

recvData=clientScoket.recv(1024)
print('recvData:%s'%recvData)

clientScoket.close()
