#-*-coding:utf-8-*-

from  socket import *


ip_address=input('请输入ip地址：')
ip_port=input('请输入端口号:')

#创建套接字
client_socket=socket(AF_INET,SOCK_STREAM)

client_socket.connect((ip_address,int(ip_port)))

print('输入q退出！')
while True:
    message=input('请输入要发送的数据：')
    if message=='q':
        break
    
    client_socket.send(message.encode('utf-8'))

    # recv_data=client_socket.recv(1024)
    # print('recv_data:%s'%recv_data)

client_socket.close()    