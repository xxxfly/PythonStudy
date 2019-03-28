# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
from multiprocessing import Pool
import os,time,random
import subprocess
import threading,multiprocessing


#print('Process (%s) start...' % os.getpid())
#Only work on UNIX/lINUX/MAC
# pid=os.fork()
# if pid==0:
#     print('I am child process (%s) and my parent is %s ' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(),pid))


# multiprocessing 模块就是跨平台版本的多进程模块
# Process 创建进程
# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name,os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# Pool
# 进程池批量创建子进程
# join() 方法会等待所有子进程执行完毕，调用之前必须调用 close()
# 调用close() 之后就不能继续添加新的 Process 了
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('Task %s runs %0.2f secondes' % (name,(end-start)))

# if __name__=='__main__':
#     print('Parent process %s' % os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')


# 子进程
# subprocess 模块
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# 
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))  #decode 有问题
# print('Exit code:', p.returncode)



# 进程间通信
# Queue

# # 写数据进程执行的代码
# def write(q):
#     print('Process to write:%s' % os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
# # 读数据进程执行的代码
# def read(q):
#     print('Process to read:%s' % os.getpid())
#     while True:
#          value=q.get(True)
#          print('Get %s from queue.' % value)

# if __name__=='__main__':
#     #父进程创建 Queue，并传给各个子进程
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     #启动子进程pw，写入
#     pw.start()
#     #启动子进程pr,读写
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()


# 线程
# _thread 是低级模块，threading 是高级模块。
# current_thread() 返回当前线程的实例
# 新线程执行的代码
# def loop():
#     print('thread %s is running...'% threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
# print('thrad %s is running...' % threading.current_thread().name)
# t=threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)


# 多线程与多进程的区别
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响。而在线程中，所有变量都有所有线程共享，任何一个变量都可以被任何一个线程修改。


# Lock
# 锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁。
# balance=0
# lock=threading.Lock()
# def change_it(n):
#     #先存后取，结果应该为0
#     global balance
#     balance=balance+n
#     balance=balance-n
# def run_thread(n):
#     for i in range(1000000):
#         #先要获取锁
#         lock.acquire()
#         try:
#             #可以放心更改
#             change_it(n)
#         finally:
#             #改完了就释放锁
#             lock.release()   
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# 当多个线程同时执行 lock.acquire() 时，只有一个线程能成功的获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。


#多核CPU
# def loop():
#     x=0
#     while True:
#         x=x^1

# print(multiprocessing.cpu_count())
# for i in range(multiprocessing.cpu_count()):
#     t=threading.Thread(target=loop)
#     t.start()

# ThreadLocal
# Threadlocal 虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# 创建全局ThreadLocal对象
local_school=threading.local()

def process_student():
    #获取当前线程关联的student
    std=local_school.student
    print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
print('Thread ended')

