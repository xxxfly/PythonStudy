#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates=["Michael","Bob","Tracy"]
print(classmates)
# print(classmates[1])
# print(len(classmates))
# print(classmates[-3])

classmates.append('Adam')
print(classmates)
classmates.insert(1,'Jack')
print(classmates)

classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

classmates[1]='Sarah'
print(classmates)

classmates2=('Michael','Bob','Tracy')
print(classmates2)
t=()
print(t)
t=(1,)
print(t)
t=('a','b',['A','B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)