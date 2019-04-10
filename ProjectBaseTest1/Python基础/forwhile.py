#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names=['Michael','Bob','Tracy']
for name in names:
    print(name)

names2=('Michael','Bob','Tracy')
for name in names:
    print(name)

sum=0
for x in range(101):
    sum+=x
print(sum)

xlist=list(range(5))
print(xlist)

sum=0
n=99
while n>0:
    sum+=n
    n-=2
print(sum)

for name in names:
    print('hello,%s'%(name))