#-*-coding=utf-8-*-
from socket import *
from time import sleep

def main():
    serSocket=socket(AF_INET,SOCK_STREAM)

    # 重复使用绑定的信息
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    localAddr = ('', 7788)

    serSocket.bind(localAddr)

    serSocket.listen(5)

    #让这个scoket 变为非阻塞
    serSocket.setblocking(False)

    #用来保存所有已经链接的客户端的信息
    clientAddr_list=[]

    while True:
        try:
            #print('-----主进程，，等待新客户端的到来------')
            #等待一个新的客户端到来，即完成三次握手的客户端
            clientSocket,client_Addr = serSocket.accept()

            #print('-----主进程，，接下来负责数据处理[%s]-----'%st(client_Addr))       
        except:
            pass
        else:
            print('---一个新的客户端到来：%s'%str(client_Addr))
            clientSocket.setblocking(False)
            clientAddr_list.append((clientSocket,client_Addr))
        
        for clientSocket,clientAddr in clientAddr_list:
            try:
                recvData=clientSocket.recv(1024)
            except:
                pass
            else:
                if len(recvData)>0:
                    print('%s:%s'%(str(clientAddr),recvData))       
                else:
                    clientSocket.close()
                    clientAddr_list.remove((clientSocket,clientAddr))
                    print('%s 已经下线'%(str(clientAddr)))    
    serSocket.close()

if __name__ == '__main__':
    main()