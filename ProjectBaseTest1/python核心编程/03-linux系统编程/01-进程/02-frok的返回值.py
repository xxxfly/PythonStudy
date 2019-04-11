# coding:utf-8

import os
import time

#程序执行到os.fork()的时候，会创建一个新的进程（子进程），然后将父进程的所有信息
#复制到子进程中。 父进程和子进程都会从fork()函数中得到一个返回值，在子进程的值一定
#是0，而父进程中是子进程的ID号
ret=os.fork()
#打印两次 ‘haha’
#print('haha')
 

# 打印 1 和 2 同时执行
# if ret==0:
#     while True:
#         print('---1---')
#         time.sleep(1)
# else:
#     while True:
#         print('---2---')
#         time.sleep(1)

print(ret)
if ret>0:
    print('---父进程---%d-'%os.getpid())
else:
    print('---子进程---%d-%d-'%(os.getpid(),os.getppid()))

