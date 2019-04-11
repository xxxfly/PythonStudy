#coding:utf-8
#import socket
from socket import *

#socket简介
#本地的进程见通信：队列，同步（互斥锁、条件变量）

#网络中进程之间如何通信
#cocket 简称 套接字，是进程间通信的一种方式。

# tcp套接字
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
print('tcp Socket Created')
#udp 套接字
s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('udp Socket Created')


#1.创建套接字
udpScoket=socket(AF_INET,SOCK_DGRAM)

#2.准备接收方的地址
sendAddr=('192.168.1.103',8080)

#3.从磁盘获取数据
sendData=raw_input("请输入要发送的数据；")

#4.发送数据到指定的电脑上
udpScoket.sendto(sendData,sendAddr)

#5.关闭套接字
udpScoket.close()


