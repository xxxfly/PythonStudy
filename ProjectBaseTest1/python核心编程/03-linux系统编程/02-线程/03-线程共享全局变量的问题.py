#coding:utf-8

from threading import Thread
import time

g_num=0
def work1():
    global g_num
    for i in range(100000):
        g_num+=1
    print('---in work1---g_num=%d'%g_num)

def work2():
    global g_num
    for i in range(100000):
        g_num+=1
    print('---in work2---g_num=%d'%g_num)


if __name__ == '__main__':
    t1=Thread(target=work1)
    t1.start()

    #time.sleep(3) #取消屏蔽之后，再次运行程序，结果会不一样

    t2=Thread(target=work2)
    t2.start()

    