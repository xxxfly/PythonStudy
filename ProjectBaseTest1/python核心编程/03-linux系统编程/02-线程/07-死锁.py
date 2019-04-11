#coding:utf-8

import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name+'--do1--up--')
            time.sleep(1)

            if mutexB.acquire():#在等待mutexB释放，但是MyThread2却要等待mutexA释放。此时进入死锁状态
                print(self.name+'--do1--down--')
                mutexB.release()
            mutexA.release()
        

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name+'--do2--up--')
            time.sleep(1)

            if mutexA.acquire(): #在等待mutexA释放，但是MyThread1却要等待mutexB释放。此时进入死锁状态
                print(self.name+'--do2--down--')
                mutexA.release()
            mutexB.release()

mutexA=threading.Lock()
mutexB=threading.Lock()
    

if __name__ == '__main__':
    t1=MyThread1()
    t2=MyThread2()
    t1.start()
    t2.start()
