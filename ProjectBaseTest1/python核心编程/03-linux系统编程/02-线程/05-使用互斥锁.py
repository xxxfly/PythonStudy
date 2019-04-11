#coding:utf-8

from threading import Thread,Lock
import time

# g_num=0
# def work1():
#     global g_num
#     #这个线程和work2 线程都在抢着对这个锁 进行上锁，如果有一方成功上锁，那么导致另外
#     #一方会堵塞（一直等待），到这个锁被解开为止
#     mutex.acquire()
#     for i in range(100000):
#         g_num+=1 
#     #用来对mutex指定的这个锁，进行解锁，，，只要开了锁，那么接下来会让所有因为这个锁
#     #被上了锁而堵塞的线程，进项抢着上锁
#     mutex.release()       
#     print('---in work1---g_num=%d'%g_num)

# def work2():
#     global g_num
#     mutex.acquire()
#     for i in range(100000):
#         g_num+=1
#     mutex.release()            
#     print('---in work2---g_num=%d'%g_num)


# if __name__ == '__main__':
    
#     #创建一把互斥锁，这个锁默认是没有上锁的
#     mutex=Lock()

#     t1=Thread(target=work1)
#     t1.start()
    
#     #time.sleep(3) #取消屏蔽之后，再次运行程序，结果会不一样

#     t2=Thread(target=work2)
#     t2.start()



#---------
#互斥锁放在for循环里面
g_num=0
def work1():
    global g_num
    #这个线程和work2 线程都在抢着对这个锁 进行上锁，如果有一方成功上锁，那么导致另外
    #一方会堵塞（一直等待），到这个锁被解开为止
    for i in range(100000):
        mutex.acquire()
        g_num+=1 
        mutex.release() 
    #用来对mutex指定的这个锁，进行解锁，，，只要开了锁，那么接下来会让所有因为这个锁
    #被上了锁而堵塞的线程，进项抢着上锁
          
    print('---in work1---g_num=%d'%g_num)

def work2():
    global g_num    
    for i in range(100000):
        mutex.acquire()
        g_num+=1
        mutex.release()            
    print('---in work2---g_num=%d'%g_num)


if __name__ == '__main__':
    
    #创建一把互斥锁，这个锁默认是没有上锁的
    mutex=Lock()

    t1=Thread(target=work1)
    t1.start()
    
    #time.sleep(3) #取消屏蔽之后，再次运行程序，结果会不一样

    t2=Thread(target=work2)
    t2.start()

    