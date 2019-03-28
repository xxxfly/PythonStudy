# -*- coding: utf-8 -*-

# foo=lambda x:x+1
# print(foo(3))
# print(foo)

# def test1():
#     print('--1--')
# def test1():
#     print('--2--')
# #函数名相同，会取最下面的函数
# test1()

#装饰器
# def check(func):
#     def inner():
#         print('--正在验证权限--')
#         if True:
#             func()
#         else:
#             print('没有权限')
#     return inner
    

# # f1=check(f1)  
# @check
# def f1():
#     print('--f1--')
# @check
# def f2():
#     print('--f2--')

# # innerFunc=check(f1)
# # innerFunc()

# # f1=check(f1)
# # f1()

# f1()
# f2()

# #装饰器例子
# def makeBlod(fn):
#     def wrapped():
#         print('--1--')
#         return '<b>'+fn()+'</b>'
#     return wrapped
# def makeItalic(fn):
#     def wrapped():
#         print('--2--')
#         return '<i>'+fn()+'</i>'
#     return wrapped

# @makeBlod  #先执行 makeBlod  发现执行 return 的时候，fn() 对象还有装饰器，所以就去执行makeItalic
# @makeItalic  # 执行 makeItalic 到return 的时候，遇到 fn 就去执行 test3 将执行的结果返回到 makeItalic ，再去回去执行 makeBlod 的return 
# def test3():
#     print('--3--') 
#     return "hello wlord--3"
# ret=test3()
# print(ret)


#装饰器例子-什么时候执行装饰器
# def check(func):
#     print("--正在装饰--")
#     def inner():
#         print('--正在验证权限--')
#         if True:
#             func()
#         else:
#             print('没有权限')
#     return inner
# # f1=check(f1)  
# @check  #即使还没有使用 f1(), 只要python 解释器执行到这里，就好自动进行装饰，不是等到调用的f1()的时候才装饰
# def f1():
#     print('--f1--')

# # innerFunc=check(f1)
# # innerFunc()

# # f1=check(f1)
# # f1()
# #在调用f1之前，已经进行装饰了
# #f1()


# #装饰器-强调
# def w1(func):
#     print('--正在装饰1--')
#     def inner():
#         print('--正在验证权限1--')
#         func()
#     return inner
# def w2(func):
#     print('--正在装饰2--')
#     def inner():
#         print('--正在验证权限2--')
#         func()
#     return inner
# #只要python解释器执行到了这里，就会自动进行装饰，而不是等到调用的时候才装饰的
# #装饰器装饰的时候，是从下往上装饰
# @w1 #f1=w1(f1) (2) 此时 f1 指向的是 w1 里面的 inner ,也是没有执行
# @w2 #f1=w2(f1) (1) 此时f1 指向的是 w2 里面的 inner ,但是没有执行  
# def f1():
#     print('--f1--')
# #装饰器调用的时候，是从上往下调用的
# f1()


# 装饰器-无参数的函数进行装饰
# def useOnce(funcName):
#     print('--useOnce--1--')
#     def func_in():
#         print('--func_in--1--')
#         funcName()
#         print('--func_in--2--')
#     print('--useOnce--2--')
#     print('--useOnce--3--')
#     return func_in

# @useOnce
# def test():
#     print('--test--')

# # test=useOnce(test)
# # test()

# test()


#装饰器-有参数的函数进行装饰
# def useOnce(funcName):
#     print('--useOnce--1--')
#     def func_in(aa,bb):
#         print('--func_in--1--')
#         funcName(aa,bb)
#         print('--func_in--2--')
#     print('--useOnce--2--')
#     print('--useOnce--3--')
#     return func_in

# @useOnce
# def test(a,b):
#     print('--test--a=%d,b=%d'%(a,b))
# # test=useOnce(test)
# # test()

# test(1,3)

#装饰器-有参数的函数进行装饰
# def useOnce(funcName):
#     print('--useOnce--1--')
#     def func_in(*args,**kw):
#         print('--func_in--1--')
#         funcName(*args,**kw)
#         print('--func_in--2--')
#     print('--useOnce--2--')
#     print('--useOnce--3--')
#     return func_in

# @useOnce
# def test(a,b,c):
#     print('--test--a=%d,b=%d,c=%d'%(a,b,c))
# # test=useOnce(test)
# # test()

# test(1,3,8)


#装饰器-对带有返回值的函数进行装饰
# def useOnce(funcName):
#     print('--useOnce--1--')
#     def func_in():
#         print('--func_in--1--')
#         return funcName()
#         #print('--func_in--2--')
#     print('--useOnce--2--')
#     print('--useOnce--3--')
#     return func_in

# @useOnce
# def test():
#     print('--test--')
#     return 'haha'

# #没有装饰器的时候
# # ret=test()
# # print('test return value is %s'%ret)
# #有装饰器的时候
# ret=test()
# print('test return value is %s'%ret)

# #装饰器-通用装饰器
# def useOnce(funcName):    
#     def func_in(*args,**kw):        
#         return funcName(*args,**kw)                
#     return func_in

# #带返回值的函数
# @useOnce
# def test():
#     print('--test--')
#     return 'haha'
# #不带返回值的函数
# @useOnce
# def test2():
#     print('--test2--')
# #带参数的函数
# @useOnce
# def test3(a):
#     print('--test3--a=%d'%a)


# #没有装饰器的时候
# # ret=test()
# # print('test return value is %s'%ret)
# #有装饰器的时候
# ret=test()
# print('test return value is %s'%ret)
# test2()
# test3(3)


#装饰器-带有参数的装饰器
def useOnce_arg(arg):
    def useOnce(funcName):    
        def func_in(*args,**kw):
            print('--记录日志--arg=%s'%arg)        
            return funcName(*args,**kw)                
        return func_in
    return useOnce

#1.下执行useOnce_arg('haha')函数，这个函数return 的结果是 userOnce 这个函数的引用
#2.@userOnce
#3.使用userOnce进行装饰
@useOnce_arg('haha')
def test():
    print('--test--')

test()



