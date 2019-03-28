# -*- coding: utf-8 -*-
import copy

# #浅拷贝
# a=[1,2,3]
# b=a   #b只是指向了a的指向地址
# print(id(a))
# print(id(b))
# a.append(4) #a指向的内容发生变化，则b指向的内容也发生变化
# print('a:%s'%a) 
# print('b:%s'%b)


# #深拷贝
# c=copy.deepcopy(a)  #c直接拷贝了 a指向的内容，创建自己指向的内容
# print(id(c))
# print('a:%s'%a) 
# print('c:%s'%c)
# a.append(5) #a指向的内容发生变化，但是c指向的内容不发生变化
# print('c:%s'%c) 


# # 数组拷贝
# a=[1,2,3]
# b=[4,5,6]
# c=[a,b]  #c创建了数组的，但是数组里面分别指向了a和b指向的内容
# #浅拷贝
# d=c
# print(id(c))
# print(id(d))
# #深拷贝
# e=copy.deepcopy(c) #c指向了一片新的内存地址
# print(id(e))
# a.append(7)   #c指向的内容和d指向的内容都发生改变，但是e指向的内容不会发生改变
# print('c:%s'%c)
# print('d:%s'%d)
# print('e:%s'%e)

#元组拷贝
a=[1,2,3]
b=[4,5,6]
c=(a,b)
#深拷贝
e=copy.deepcopy(c)
print(id(c))
print(id(e))
print(c)
print(e)
a.append(7) #c指向的内容发生改变，但是e指向的内容不会发生改版
print(c)
print(e)
#浅拷贝
d=copy.copy(c)
print(id(c)) #c和d的id一样
print(id(d))
print(c)
print(d)
a.append(8) #c指向的内容发生改变，d指向的内容也发生改版
print(c)
print(d)



# #数组浅拷贝
# a=[1,2,3]
# b=[4,5,6]
# c=[a,b]
# d=copy.copy(c)
# print(id(c)) #但是c和d的id不一样
# print(id(d))
# print(c)
# print(d)
# a.append(8) #c指向的内容发生改变，d指向的内容也发生改版
# print(c)
# print(d)



