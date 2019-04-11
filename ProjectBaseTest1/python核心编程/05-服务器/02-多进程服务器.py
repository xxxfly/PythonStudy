#-*-coding=utf-8-*-
from socket import *
from multiprocessing import *
from time import sleep


# 处理客户端的请求并执行事情
def delwithCLient(newSocket,destAddr):
    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData)>0:
                print('recv[%s]:%s'%(str(destAddr), recvData))
            else:
                print('[%s]客户端已经关闭'%str(destAddr))
                break
    finally:
        newSocket.close()



def main():
    serSocket=socket(AF_INET,SOCK_STREAM)

    # 重复使用绑定的信息
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    localAddr = ('', 7788)

    serSocket.bind(localAddr)

    serSocket.listen(5)

    try:
        while True:
            
            print('-----主进程，，等待新客户端的到来------')

            newSocket,destAddr = serSocket.accept()

            print('-----主进程，，接下来负责数据处理[%s]-----'%str(destAddr))
            
            client=Process(target=delwithCLient,args=(newSocket,destAddr))
            client.start()

            #因为已经向子进程中copy了一份（引用），并且父进程中这个套接字也没有用处了
            #所以关闭
            newSocket.close()

    finally:
        serSocket.close()

if __name__ == '__main__':
    main()