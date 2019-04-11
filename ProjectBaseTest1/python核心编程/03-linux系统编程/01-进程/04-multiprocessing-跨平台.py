# coding:utf-8

from multiprocessing import Process
import time
#fork 只能用于 Unix/Linux,不能在windows执行
#multiprocessing模块可以实现在windows上执行多进程

def test():
    while True:
        print('--test--')
        time.sleep(1)

p=Process(target=test)
p.start() #让这个进程开始执行test函数里面的代码

while True:
    print('--main--')
    time.sleep(1)
