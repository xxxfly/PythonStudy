#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Bob'])
d['Adam']=87
print(d['Adam'])
print('Adam' in d)
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas',-1))

d.pop('Bob')


s=set([1,2,3])
print(s)
s=set([1,2,3,3,4,4,5])
print(s)
ss=set([2,1,3])
print(ss)
s.add(4)
print(s)
s.remove(4)
print(s)


s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)

a=['b','c','a']
a.sort()
print(a)

b='abc'
b.replace('a','A')
print(b)