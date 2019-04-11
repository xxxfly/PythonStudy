#coding:utf-8
#import socket
from socket import *


#1.创建套接字
udpScoket=socket(AF_INET,SOCK_DGRAM)

ipAddress=input('请输入IP:')
port=input("请输入端口:")

#2.准备接收方的地址
sendAddr=(ipAddress,int(port))
print('输入q退出')
while True:
    #3.从键盘获取数据
    sendData=input("请输入要发送的数据：")
    if sendData=='q':
        break
    #4.发送数据到指定的电脑上
    udpScoket.sendto(sendData.encode('utf-8'),sendAddr)
    print('已经发送。。。')

#5.关闭套接字
udpScoket.close()



#udp
#udp--用户数据报协议，是一个无链接的简单的面向数据报的运输协议。不可靠，只把应用程序传给IP层的数据报发送出去，但是并不能保证它们能到达目的地。但是，传输速度快。



#udp网络程序-发送、接收数据

# #1.创建套接字
# udpScoket=socket(AF_INET,SOCK_DGRAM)

# #2.准备接收方的地址
# sendAddr=('192.168.1.103',8080)

# #3.从键盘获取数据
# sendData=raw_input('请输入要发送的数据：')

# #4.发送数据到指定的电脑上
# udpScoket.sendto(sendData,sendAddr)

# #5.等待接收对方的数据
# recvData=udpScoket.recvfrom(1024) #1024表示本次接收的最大字节数

# #6.显示对方发送的数据
# print(recvData)

# #7.关闭套接字
# udpScoket.close()


#绑定信息
# #1.创建套接字
# udpScoket=socket(AF_INET,SOCK_DGRAM)

# #2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
# bindAddr=('',7788) #ip地址和端口号，ip一般不用写，表示本地的任何一个ip
# udpScoket.bind(bindAddr)

# #3.等待接收对方发送的数据
# recvData=udpScoket.recvfrom(1024) #1024表示本次接收的最大字节数

# #4.显示接收到的数据
# print(recvData)

# #5.关闭套接字
# udpScoket.close()


#接收信息
# udpScoket=socket(AF_INET,SOCK_DGRAM)

# udpScoket.bind(('',7788))

# recvData=udpScoket.recvfrom(1024)

# print(recvData) #('content',('192.168.1.128',2426))


#python3 发送字节
#udpScoket.sendto(sendData.encode('utf-8'),('',8080))



