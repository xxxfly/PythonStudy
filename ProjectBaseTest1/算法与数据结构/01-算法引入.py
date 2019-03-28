#-*- coding:utf-8 -*-
import time
from timeit import Timer


#题1：已知a+b+c=100, a*a+b*b=c*c(a,b,b为自然数)，求a,b,c的组合
#枚举法
# start_time=time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print('a=%d,b=%d,c=%d'%(a,b,c))

# end_time=time.time()
# print('times:%d'%(end_time-start_time))
# print('finished')

#T=1000*1000*1000*2 执行步骤
#T(n)=n^3*2 

# #改进
# start_time=time.time()
# for a in range(1001):
#     for b in range(1001):
#         c=1000-a-b    
#         if a**2+b**2==c**2:
#             print('a=%d,b=%d,c=%d'%(a,b,c))

# end_time=time.time()
# print('times:%d'%(end_time-start_time))
# print('finished')



# a=[3,2,1,5,32,33,12,44,19] #无序数列排序，最多 n^2 次操作
# b=[1,2,3,4,5,6,7,8]  #有序序列排序，就n次操作



#代码执行时间测量模块
#timeit模块
#class timeit.Timer(stmt='',setip='',timer=<timer function>)
#stmt 是要测试的代码语句 ； setup 是运行代码要设置的参数；timer 是一个定时器函数，与平台无关

def test1():
    li=[]
    for i in range(10000):
        li.append(i)
def test2():
    li=[]
    for i in range(10000):
        li=li+[i] #最慢
        #li+=[i] #优化
def test3(): #最快
    li=[i for i in range(10000)]
def test4():
    li=list(range(10000))
def test5():
    li=[]
    for i in range(10000):
        li.extend([i])
def test6():  #非常慢
    li=[]
    for i in range(10000):
        li.insert(0,i)

timr1=Timer("test1()","from __main__ import test1")
print("append:",timr1.timeit(1000)) 
timr2=Timer("test2()","from __main__ import test2")
print("+:",timr2.timeit(1000)) 
timr3=Timer("test3()","from __main__ import test3")
print("[i for i in range]:",timr3.timeit(1000)) 
timr4=Timer("test4()","from __main__ import test4")
print("list(range()):",timr4.timeit(1000)) 
timr5=Timer("test5()","from __main__ import test5")
print("extend:",timr5.timeit(1000)) 
timr6=Timer("test6()","from __main__ import test6")
print("insert:",timr6.timeit(1000)) 


