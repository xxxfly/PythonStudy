#coding:utf-8

from threading import Thread
from socket import *

def sendData():
    """发送数据""""    
    while True:
        sendInfo=input('<<')
        udpSocket.sendto(sendInfo.encode('utf-8'),(toIP,toPort))

def receiveData():
    """接收数据"""    
    while True:
        recvInfo=udpSocket.recvfrom(1024)
        content,ipInfo=recvInfo
        print('>>%s-%s-:%s'%(str(time.time()),str(ipInfo),content.decode('utf-8')))        
    
    udpSocket.close()

udpSocket=None
toIP=''
toPort=0

def charMain():
    """聊天室"""
    global udpSocket
    global toIP
    global toPort
    toIP=input('对方的IP:')
    toPort=input('对方的端口:')
    
    udpSocket=socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(('',6907))

    ts=Thread(target=sendData)
    tr=Thread(target=receiveData)

    ts.start()
    tr.start()

    ts.join()
    tr.join()
    
    
if __name__ == '__main__':
    charMain()