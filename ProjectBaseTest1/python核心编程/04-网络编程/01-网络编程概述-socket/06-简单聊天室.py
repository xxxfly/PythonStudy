#coding:utf-8

from socket import *
import time


def charMain():
    #聊天室
    udpSocket=socket(AF_INET,SOCK_DGRAM)

    udpSocket.bind(('',3900))

    while True:
        recvData=udpSocket.recvfrom(1024)
        content,ipInfo=recvData
        print('%s-%s-消息:%s'%(str(time.time()),str(ipInfo),content.decode('utf-8')))        
    
    udpSocket.close()
    
if __name__ == '__main__':
    charMain()