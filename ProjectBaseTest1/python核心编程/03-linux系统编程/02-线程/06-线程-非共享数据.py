#coding:utf-8

from threading import Thread
import threading
import time

#函数里面的变量各自是各自的
def work1():
    name=threading.current_thread().name
    print('---thread name is %s'%name)
    g_num=100
    if name=='Thread-1':
        g_num+=1
    else:
        time.sleep(2)
    print('---thread is %s---g_num=%d'%(name,g_num))
    

def work2():
    time.sleep(1)
    g_num=100
    print('---in work2---g_num=%d'%g_num)


if __name__ == '__main__':
    t1=Thread(target=work1)
    t1.start()

    # t2=Thread(target=work2)
    # t2.start()

    t2=Thread(target=work1)
    t2.start()
    