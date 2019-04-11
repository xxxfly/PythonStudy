#coding:utf-8

from socket import *
import struct

#1.什么叫下载
# 2.怎样完成下载？
#   1.创建一个空文件
#   2.向里面写数据
#   3.关闭
# 3.什么叫上传

udpSocket=socket(AF_INET,SOCK_DGRAM)


f=open('test.jpg','wb')

while True:
    
    recvData=udpSocket.recvfrom(1024)
    f.write('')


f.close()

#4.怎么发送，怎么接收
#    使用fttp协议

#5.什么情况下知道服务器已经发送完毕
#  如果接收到的数据长度少于516（2个字节操作码+2个直接的序号+512字节数据）时，意味着服务器发送完毕

#6.怎么样保证一个数字占用2个字节呢

sendData=struct.pack('!H8sb5sb',1,'test.jpg',0,'octet',0)

udpSocket=socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(sendData,('192.168.31.239',69))

udpSocket.close()



#解包
#result=struct.unpack('!H',sendData[:4])
#print(result)
