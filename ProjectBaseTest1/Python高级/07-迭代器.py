# -*- coding: utf-8 -*-

from collections import Iterable,Iterator

#可迭代对象  能够使用for循环的对象是可迭代对象；生成器generator也是可以迭代的 

print(isinstance([],Iterable))
print(isinstance('asd123',Iterable))
print(isinstance({"a":1,"b":2},Iterable))
print(isinstance(100,Iterable))

#迭代器  可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
print(isinstance([1,2,3,4],Iterator))
print(isinstance((x for x in range(10)),Iterator))

#生成器都是Iterator对象

#iter()  将Iterable变成Iterator对象

a=[1,2,3,4]
print(type(a))
b=iter(a)
print(type(b))
print(next(b))
print(next(b))
print(next(b))
