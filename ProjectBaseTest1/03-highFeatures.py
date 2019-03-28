# -*- coding: utf-8 -*-
import os
from collections import Iterable
from collections import Iterator
L=['Michael','Sarah','Tracy','Bob','Jack']
r=[]
n=3
for i in range(n):
    r.append(L[i])

print(r)
print(L[0:3])
print(L[:3])
print(range(3))
print(L[-2:])
print(L[-3:-1])
print(L[-1:])

print((0,1,2,3,4,5,6)[:3])
print((0,1,2,3,4,5,6,7,8,9,10)[:10:2])
print('ABCDEF'[:3])

def trim(str):
    if str[0]==' ':
        return trim(str[1:])
    elif str[-1]==' ':
        return trim(str[:-1])
    else:
        return str
print(trim('  asd asda '))
print(trim('asd asda '))
print(trim('  asd asda'))

for item in L:
    print(item)

d={'a':1,'b':2,'c':3}
for key in d:
    print(key)

for ch in 'ABCD':
    print(ch)


print(isinstance('abc',Iterable))
print(isinstance([123],Iterable))
print(isinstance(123,Iterable))

for i,value in enumerate(['A','b','C']):
    print(i,value)

for x,y in[(1,1),(3,4),(5,9)]:
    print(x,y)

def findMinAndMax(L):
    max=None
    min=None
    if  isinstance(L, Iterable)==False:
        return min,max
    max=L[0]
    min=L[0]
    for v in L:
        if max<v:
            max=v
        if min>v:
            min=v
    return min,max

print(findMinAndMax([3,5,2,8,9]))

print(list(range(1,10)))           
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'ABC' for n in '123'])

print([d for d in os.listdir('.')])

d={'a':'1','b':'2','c':'3'}
for k,v in d.items():
    print(k,'=',v)

print([k+'='+v for k,v in d.items()])

L1=['Hello','World',18,'Apple',None]
print([s.lower() for s in L1 if isinstance(s,str)])

g=(x*x for x in range(10))
print(g)
print('n',next(g))
print('n',next(g))
print('n',next(g))
print('n',next(g))
for n in g:
    print(n)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print('1-',b)
        a,b=b,a+b
        n=n+1
    return 'done'
fib(6)

def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib2(6)
print(f)
for n in fib2(6):
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o=odd()
print(next(o))
print(next(o))
print(next(o))

while True:
    try:
        x=next(f)
        print('g：',x)
    except StopIteration as e:
        print('Generator return value：',e.value)
        break

def triangles():
    l = [1]
    while 1:
        yield l
        l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1] 
    
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break


print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))


print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))

