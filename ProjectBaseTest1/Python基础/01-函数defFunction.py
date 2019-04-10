#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        return TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
    
x=my_abs('A')
print(x)

def nop():
    pass

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

x,y=move(100,100,60,math.pi/6)
print(x,y)
print(move(100,100,60,math.pi/6))

print(len('5047169270716166'))


def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and not isinstance(b,(int,float)) and not isinstance(c,(int,float)):
        return TypeError('bad operand type')
    if a==0:
        return 'no ansewr'
    x1=(-b+math.sqrt((b*b-4*a*c)/(4*a*a)))/(2*a)
    x2=(-b-math.sqrt((b*b-4*a*c)/(4*a*a)))/(2*a) 
    return x1,x2
print(quadratic(1,-4,2))

def power(x):
    return x*x

def power1(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

def power2(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('Sarch','F',city='TianJin')

def add_end(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
# print(calc([2,3,5,6]))
print(calc(1, 3, 5, 7))
print(calc(*[2,3,5,6]))

def person(name,age,**kw):
    print('name:',name,'age:',age,'other',kw)

person('Michael',24)
person('Michael',24,city='BeiJing')
person('Michael',24,city='BeiJing',job='Enginner')

extra={'city':'BeiJing','job':'Engineer'}
person('Michael',24,city=extra['city'],job=extra['job'])
person('Michael',24,**extra)

def person2(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name：',name,'age：',age,'other：',kw)

person2('Michael',24,city='Beijing',addr='Chaoyang',zipcode=123456)

def person3(name,age,*,city,job):
    print(name,age,city,job)

person3('Michael',24,city='Beijing',job='Engineer')


def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)

def product(*numbers):
    if numbers==():
        raise TypeError
    result=1
    for x in numbers:
        result=result*x
    return result

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

def fetch(n):
    if n==1:
        return 1
    return n*fetch(n-1)
print(fetch(5)) 
#print(fetch(100))   

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product) 

print(fact(5))

def move1(n,a,b,c):
    if n==1:
        print(a,'-->',c)#a上只有1个盘子
    else:#a上有2个盘子
        move1(n-1,a,c,b)#把a上的n-1块移动到b
        move1(1,a,b,c)#把a上的最后一块移动到c
        move1(n-1,b,a,c)#把b上的n-1块移动到c
    
move1(5,'A','B','C')
