# coding:utf-8

import os
import time

#程序执行到os.fork()的时候，会创建一个新的进程（子进程），然后将父进程的所有信息
#复制到子进程中。 父进程和子进程都会从fork()函数中得到一个返回值，在子进程的值一定
#是0，而父进程中是子进程的ID号
#ret=os.fork()
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

# print(ret)
# if ret>0:
#     print('---父进程---%d-'%os.getpid())
# else:
#     print('---子进程---%d-%d-'%(os.getpid(),os.getppid()))

#父子进程的先后
# if ret==0:
#     print('---子进程1---')
#     time.sleep(5)
#     print('---子进程2---')
# else:
#     print('---父进程---')
#     time.sleep(3)
# print('---over---')

#先执行哪个进程，看系统调度
# if ret==0:
#     print('haha1')
# else:
#     print('haha2')


#-----------------------------
#修改全局变量
#每一个进程都是各自的数据，互不影响
# g_num=100
# ret=os.fork()
# if ret==0:
#     print('--process-1--')
#     g_num+=1
#     print('--process-1 g_num=%d'%g_num)
# else:
#     time.sleep(3)
#     print('--process-2--')
#     print('--process-2 g_num=%d'%g_num)


#多次fork的问题
# #父进程
# ret=os.fork()
# if ret==0:
#     #子进程
#     print('--1--')
# else:
#     #父进程
#     print('--2--')

# #父子进程
# ret=os.fork()
# if ret==0:
#     #孙子
#     #2儿子
#     print('--11--')
# else:
#     #儿子
#     #父进程
#     print('--22--')

# ret=os.fork()
# #父进程
# if ret==0:
#     #子进程
#     print('--1--')
# else:
#     #父进程
#     print('--2--')
#     ret=os.fork()
#     if ret==0:
#         #2儿子
#         print('--11--')
#     else:
#         #父进程
#         print('--22--')

ret=os.fork()
ret=os.fork()
ret=os.fork()

#会执行八次
print('---1---')


