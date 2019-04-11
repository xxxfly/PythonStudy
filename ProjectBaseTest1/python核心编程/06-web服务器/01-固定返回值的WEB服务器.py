#-*-coding:utf-8-*-

import socket
from multiprocessing  import *
from time import sleep
import re


# 设置静态文件的更目录
HTML_ROOT_DIR='./page'



def delwidthClient(newSocket,destAddr):
    """处理客户端请求"""
    try:
        
        # 获取客户端请求的数据
        recvData=newSocket.recv(1024)
        if len(recvData)>0:
            print('recv[%s]:%s'%(str(destAddr),recvData))
            # 解析HTTP报文数据 request_data
            request_lines=recvData.splitlines()
            for line in request_lines:
                print(line)
            # 提取请求方式            
            request_start_line=request_lines[0]            
            # 提取请求路径   
            print('*'*10)   
            print(str(request_start_line))          
            file_name=re.match(r'\w+\s+(/[^\s]*)\s',request_start_line.decode('utf-8')).group(1)
            if '/' == file_name:
                file_name='/index.html'
            
            try:
                # 打开文件，读取内容
                flie=open(HTML_ROOT_DIR+file_name,'rb')
                
            except IOError:
                # 构造相应数据
                response_start_line='HTTP/1.1 404 Not Found\r\n'
                response_headers='Server:My Server\r\n'
                response_body="The file is not found"
            else:
                file_data=flie.read()
                flie.close()

                # 构造相应数据
                response_start_line='HTTP/1.1 200 OK\r\n'
                response_headers='Server:My Server\r\n'
                response_body=file_data.decode('utf-8')
            finally:

                response=response_start_line+response_headers+'\r\n'+response_body

                print('响应客户端[%s]的消息：%s'%(str(destAddr),response))

                # 向客户端返回相应数据
                newSocket.send(bytes(response,'utf-8')) 

                # 关闭客户端链接
                newSocket.close()               

        else:
            print('[%s]客户端已经关闭'%str(destAddr))
           
    finally:
        # 关闭客户端链接
        newSocket.close()

if __name__ == '__main__':
    serSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 重复使用绑定的信息
    serSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    loaclAddr=('',8899)
    serSocket.bind(loaclAddr)

    serSocket.listen(5)

    try:
        while True:
            print('---主进程，等待新的客户端链接---')
            newSocket,deskAddr=serSocket.accept()

            print('---主进程，开始处理数据[%s]'%str(deskAddr))
            # 开启一个处理进程
            client=Process(target=delwidthClient,args=(newSocket,deskAddr))
            client.start()

            # 因为已经向子进程中copy了一份（引用），并且父进程中这个套接字也没有用处了
            # 所以关闭
            newSocket.close()
    finally:
        serSocket.close()