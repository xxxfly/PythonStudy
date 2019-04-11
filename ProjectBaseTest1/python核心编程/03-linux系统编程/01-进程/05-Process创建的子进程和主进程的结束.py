# coding:utf-8

from multiprocessing import Process
import time
#fork 只能用于 Unix/Linux,不能在windows执行
#multiprocessing模块可以实现在windows上执行多进程

# def test():
#     for i in range(5):
#         print('--test--')
#         time.sleep(1)

# #等待子进程 都结束，主进程才能结束
# p=Process(target=test)
# p.start() #让这个进程开始执行test函数里面的代码


def test():
    for i in range(5):
        print('--%d--'%i)
        time.sleep(1)

#等待子进程 都结束，主进程才能结束
p=Process(target=test)
p.start() #让这个进程开始执行test函数里面的代码

#time.sleep(2)
#p.join() #堵塞  等着子进程执行结束  
p.join(1) #堵塞  等着子进程执行结束 -参数是等待的时间
p.terminate() #立刻终止
print('--main--')



