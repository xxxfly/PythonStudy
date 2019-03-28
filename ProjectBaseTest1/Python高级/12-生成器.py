# -*- coding: utf-8 -*-

# def fib(times):
#     a,b=0,1
#     for n in range(times):
#         yield b
#         a,b=b,a+b
    
# f=fib(5)
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # for num in f: #迭代器是可以用作for循环里面的
# #     print(num)

# print(f.__next__())  #等价于 next(f)



#send
# def test():
#     i=0
#     while i<5:
#         temp=yield i  #遇到yeild停止，等待下次执行时，tmp对象并没有被赋值，所以此时temp为None
#         print(temp)
#         i+=1

# t=test()
# print(next(t))
# print(next(t))
# print(next(t))
# print(t.send('haha'))  #send 也可以像next 一样获取下一个值，但是他能将 yield 整体 赋值。执行的时候就会给temp赋值。
# t=test()
# #print(t.send('haha')) #但是如果第一次就执行send的话，代码是从头开始执行的。所以 'haha' 这个值就不知道给谁了，就会报错
# print(t.send(None)) #第一次执行可以不传值
# print(t.send('haha')) #第二次就可以传值了，此时temp ='haha'
# print(t.__next__()) #但是如果再有next，也就是没有传值，此时 temp=None


# def test():
#     i=0
#     while i<5:
#         if i==0:
#             temp=yield i
#         else:
#             yield i    
#         i+=1
# t=test()
# print(t.__next__())
# print(t.send('haha'))


#多任务

def test1():
    while True:
        print('--1--')
        yield None
def test2():
    while True:
        print('--2--')
        yield None
t1=test1()
t2=test2()
i=0
while i<100:
    t1.__next__()
    t2.__next__()
    i+=1