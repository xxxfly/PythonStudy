# coding:utf-8
import os
import random
import time
from multiprocessing import Process,Pool

#fork 只能用于 Unix/Linux,不能在windows执行
#multiprocessing模块可以实现在windows上执行多进程


def worder(num):
    for i in range(5):
        print('---pid=%d---num=%d---'%(os.getpid(),num))
        time.sleep(1)

# #创建进程池，进程池中最多有3个进程一起执行
# pool=Pool(3)

# for i in range(10):
#     print('---%d---'%i)
#     #向进程池中添加任务
#     #注意：如果添加的任务数量超过了，进程池中进程的个数的话，那么不会导致添加不进入
#     #   添加到进程中的任务，如果还没有执行的话，那么此时，他们会等待进程池中的
#     #   进程完成一个任务之后，会自动的去用刚刚的那个进程，完成当前的新任务
#     pool.apply_async(worder,(i,))


# print('---start---')
# pool.close() #关闭进程池，关闭后pool不在接收新的请求
# pool.join() #等待pool中所有子进程执行完成，必须放在close语句之后。主进程 创建/添加 #            任务后，主进程默认不会等待进程池中的任务执行完后才结束，而是 当 主进程的#           任务做完之后，立马结束。如果这个地方没有join，会导致进程池中的任务不会执
# #           行
# print('---end---')




#多种方式的比较

#1.fork()
#ret=os.fork()

#2.p1=Process(target=xxx)
#p1.start()

#3.pool=Pool(3)
#pool.apply_async(xxx)
#主进程一般用来等待，真正的任务都在子进程中执行




#创建进程池，进程池中最多有3个进程一起执行
pool=Pool(3)

for i in range(10):
    print('---%d---'%i)
    #向进程池中添加任务
    pool.apply(worder,(i,)) #阻塞的方式，执行完一个，在执行一个，排队执行


print('---start---')
pool.close() #关闭进程池，关闭后pool不在接收新的请求
pool.join() #等待pool中所有子进程执行完成，必须放在close语句之后。主进程 创建/添加 #            任务后，主进程默认不会等待进程池中的任务执行完后才结束，而是 当 主进程的#           任务做完之后，立马结束。如果这个地方没有join，会导致进程池中的任务不会执
#           行
print('---end---')
