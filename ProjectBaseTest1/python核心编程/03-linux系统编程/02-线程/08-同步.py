#coding:utf-8

from threading import Thread,Lock
import time

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('--task1--')
                time.sleep(0.5)
                lock2.release()
            
class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('--task2--')
                time.sleep(0.5)
                lock3.release()
            
class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('--task3--')
                time.sleep(0.5)
                lock1.release()

lock1=Lock()
lock2=Lock()
lock2.acquire()
lock3=Lock()
lock3.acquire()

if __name__ == '__main__':
    t1=Task1()
    t2=Task2()
    t3=Task3()

    t1.start()
    t2.start()
    t3.start()
            
