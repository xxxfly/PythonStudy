#coding:utf-8
import threading




#使用全局字典
# global_dict={}

# def std_thread(name):
#     std=Student(name)
#     #把std放到全局变量global_dict中
#     global_dict[threading.current_thread()]=std
#     do_task_1()
#     do_task_2()

# def do_task_1():
#     #不传入std，而是根据当前线程查找
#     std=global_dict[threading.current_thread()]
#     pass

# def do_task_2():
#     #任何函数都可以查找当前线程的std变量
#     std=global_dict[threading.current_thread()]
#     pass



#使用ThreadLocal
#创建全局ThreadLocal对象
local_student=threading.local()

def process_student():
    #获取当前线程关联的student
    std=local_student.student
    print('Hello,%s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_student.student=name
    process_student()

if __name__=="__main__":
    t1=threading.Thread(target=process_thread,args=("张三",),name='Thread-A')
    t2=threading.Thread(target=process_thread,args=('李四',),name="Thread-B")
    t1.start()
    t2.start()

    t1.join()
    t2.join()