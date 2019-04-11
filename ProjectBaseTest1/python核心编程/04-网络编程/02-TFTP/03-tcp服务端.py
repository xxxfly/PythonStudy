#coding=utf-8
from socket import *
#tcp 传输控制协议
#upd 用户数据报协议

#tcp
#1.稳定
#2.相对udp而言慢一些
#3.web服务器都是使用tcp

#1.创建套接字
serverScoket=socket(AF_INET,SOCK_STREAM)
#绑定地址信息
serverScoket.bind(('',8899))
#
serverScoket.listen(5)

print('---1---')
#clientScoket表示新的客户端
#clientAddr表示新的客户端的链接信息
clientScoket,clientAddr=serverScoket.accept()

print('---2---')
recvData=clientScoket.recv(1024)

print('---3---')
print('%s:%s'%(str(clientAddr),recvData))

clientScoket.close()
serverScoket.close()