#-*- coding:utf-8 -*-

a=[1,22,3,1,22,33,4,35,66]
b=set(a) #去重
print(b)

#集合还支持union(联合),intersection(交),difference(差)和sysmmetric_difference(对称差集)
a=['a','b','s','s','m','r','f','c']
b=['h','b','s','f','i','o','i']

A=set(a)
B=set(b)
print(A)
print(B)
print('并集:',A|B)#并集
print('交集:',A&B)#交集
print('差集:',A-B)#差集
print('对称差集:',A^B)#对称差集
