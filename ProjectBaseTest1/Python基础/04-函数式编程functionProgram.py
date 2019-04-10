# -*- coding: utf-8 -*-
import math
from functools import reduce
import functools

# print(abs(-10))
# print(abs)
# x=abs(-10)
# print(x)
# f=abs
# print(f)
# print(f(-10))

# abs=10
# abs(-10)

# def add(x,y,f):
#     return f(x)+f(y)

# x=10
# y=-6

# f=abs
# print(add(x,y,f))


# def f(x):
#     return x*x

# r=map(f,[1,2,3,4,5,6,7,8,9])

# print(list(r))

# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# def add(x,y):
#     return x+y

# print(reduce(add,[1,3,5,7,9]))

# def fn(x,y):
#     return x*10+y

# print(reduce(fn,[1,3,5,7,9]))

# def char2num(s):
#     digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]
# print(list(map(char2num,'13579')))
# print(reduce(fn,map(char2num,'13579')))

# def normalize(name):
#     first=name[0:1].upper()
#     left=name[1:].lower()
#     return first+left
# print(list(map(normalize,['adam', 'LISA', 'barT'])))

# def prod(L):
#     def fn(x,y):
#         return x*y
#     return reduce(fn,L)
# l=[1,3,5,7,9]
# print(prod(l))

# def str2float(s):
#     pass

# def id_odd(n):
#     return n%2==1

# print(list(filter(id_odd,[1,2,3,4,5,6,7,8,9])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty,['A','B','',' ','C',None])))

# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n


# def _not_divisible(n):
#     return lambda x:x%n>0

# def primes():
#     yield 2
#     it=_odd_iter() # 初始序列
#     print('yeild n1=',next(it))
#     while True:
#         n=next(it) # 返回序列的第一个数
#         print('yeild n2=',n)
#         yield n
#         it=filter(_not_divisible(n),it)

# for n in primes():
#     if n<10:
#         print(n)
#     else:
#         break


# print(sorted([6,2,9,-10]))
# print(sorted([4,2,8,-10],key=abs))

# print(sorted(['bob','about','Zoo','Credit']))
# print(sorted(['bob','about','Zoo','Credit'],key=str.lower))


# print(sorted(['bob','about','Zoo','Credit'],key=str.lower, reverse=True))

# def calc_sum(*args):
#     ax=0
#     for n in args:
#         ax=ax+n
#     return ax

# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum

# f=lazy_sum(1,3,5,7,9)
# print(f)
# print(f())
# f1=lazy_sum(1,3,5,7,9)
# f2=lazy_sum(1,3,5,7,9)
# print(f1==f2)

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f=[]
# f=count()
# print(f[0]())
# print(f[1]())
# print(f[2]())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs=[]
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# f=[]
# f=count()
# print(f[0]())
# print(f[1]())
# print(f[2]())

# def createCounter():
#     def counter():   
#         return next(o)
#     def f():
#         i=0
#         while True:
#             i=i+1
#             yield i
#     o=f()
#     return counter

# def createCounter():
#     m=0
#     def counter():
#         nonlocal m
#         m=m+1
#         return m
#     return counter

# def createCounter():
#     s = [0]
#     def counter():
#         s[0]+=1
#         return s[0]
#     return counter

# createCounterA=createCounter()
# print(createCounterA(),createCounterA(),createCounterA())

# l=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
# print(l)

# def f(x):
#     return x*x

# lam=lambda x:x*x
# print(lam)

# def build(x,y):
#     return lambda:x*x+y*y

# def now():
#     print('2018-03-19')
# f=now
# f()
# print(now.__name__)
# print(f.__name__)

# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print('2018-03-19')
# now()

# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print('%s %s():'%(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print('2018-03-19')
# now()
#log('execute')(now)
# print(now.__name__)


print(int('12345'))
print(int('12345',base=8))
print(int('12345',base=16))
print(int('1000101',base=2))

def int2(x,base=2):
    return int(x,base)
print(int2('1000001'))
print(int2('1110101'))

int2=functools.partial(int,base=2)
print(int2('1000001'))
print(int2('1110101'))

