#coding:utf-8

#from threading import Thread
import threading
import time

#1.如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是各的
def sayHello():
    print('---hello world---')
    time.sleep(1)


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg="i'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)


def test():
    for i in range(5):
        t=MyThread()
        t.start()

if __name__=="__main__":
    # for i in range(5):
    #     t=Thread(target=sayHello)
    #     t.start()

    # t=MyThread()
    # t.start()

    test()