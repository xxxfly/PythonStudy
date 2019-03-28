# -*- coding: utf-8 -*-
from types import MethodType
from enum import Enum,unique
# from hello import Hello


# # 实例绑定属性和方法
# class Student(object):
#     pass

# def set_age(self,age):   # 定义一个函数作为实例方法
#     self.age=age
# s=Student()
# s.name='Michael'  # 动态给实例绑定一个属性
# print(s.name)
# s.set_age=MethodType(set_age,s)  # 给实例绑定一个方法 ，但是另一个实例是没有作用的
# s.set_age(25)  # 调用实例方法
# print(s.age)

# def set_score(self,score):
#     self.score=score
# Student.set_score=set_score # 给class 绑定方法
# s.set_score(88)
# print(s.score)
# s2=Student()
# s2.set_score(90)
# print(s2.score)


# # __slots__
# # __slots__ 变量，可以限制该 class 实例能添加的属性
# # 只限制对当前类实例有用，对其子类不起作用。
# class Student(object):
#     __slots__=('name','age')    # 用tuple定义允许绑定的属性名称
# s=Student()
# s.name='Michael' #绑定属性'name'
# s.age=25 #绑定属性'age'
# s.score=88  #绑定属性'score'  不能绑定


# @property 参数检查
# @property 装饰器负责把一个方法变成属性调用
# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise  ValueError('score must be an integer!')
#         if value < 0 or value >100:
#             raise  ValueError('score must between 0~100!')
#         self._score=value

# s=Student()
# s.set_score(60)
# print(s.get_score())
# s.set_score(1000)

# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an interage!')
#         if value<0 or value >100:
#             raise ValueError('score must between 0~100')
#         self._score=value
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth=value
#     @property
#     def age(self): # 只读属性
#         return 2019-self.birth

# s=Student()
# s.score=90 #实际转化为s.set_score(90)
# print(s.score)
# # s.score=101
# s.birth=1993
# print(s.age)



# # 多重继承
# # 多重继承的设计称为 MixIn,目的是给一个类增加多个功能。
# class Animal(object):
#     pass
# #大类
# class Mammal(Animal): #哺乳动物
#     pass
# class Bird(Animal): #鸟类
#     pass
# #功能类
# class RunnableMixIn(object):
#     def run(self):
#         print('Running...')
# class FlyableMinIn(object):
#     def fly(self):
#         print('Flying...')

# #各种动物
# class Dog(Mammal,RunnableMixIn): #狗
#     pass
# class Bat(Mammal,FlyableMinIn): #蝙蝠
#     pass
# class Parrot(Bird): #鹦鹉
#     pass
# class Ostrich(Bird): #鸵鸟
#     pass



# #定制类__str__
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'Student object (name:%s)'% self.name
#     __repr__=__str__  
# #print(Student('Michael'))
# s = Student('Michael')
# print(s)


# #定制类__iter__
# #斐波那契数列
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1 #初始化两个计数器a、b
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b #计算下一个值
#         if self.a>1000: #循环退出的条件
#             raise StopIteration()
#         return self.a  #返回下一个值
# for n in Fib():
#     print(n)


#定制类__getitem__
# class Fib(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# f=Fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[3])


# __getitem__ 参数可能是int ，也可能是一个切片
# class Fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             print('int')
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice): # 切片参数
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             print(L)
#             return L
# f=Fib()
# f[:10]
# # print(f)
        

#定制类__getattr__
# 动态返回一个属性
# class Student(object):
#     def __init__(self):
#         self.name='Michael'
#     def __getattr__(self,attr):
#         if attr=='score':
#             return 89   # 返回固定值
#         if attr=='age':  
#             return lambda:25 # 返回函数

# s=Student()
# print(s.name)
# print(s.score)
# print(s.age())

# 链式调用
# class Chain(object):
#     def __init__(self,path=''):
#         self._path=path
#     def __getattr__(self,path):
#         return Chain('%s/%s' %(self._path,path))
#     def __str__(self):
#         return self._path
#     __repr__=__str__

# print(Chain().status.user.timeline.list)


# 定制类 __call__
# 可以直接对实例进行调用，类似函数调用一样，
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         print('My name is %s'% self.name)

# s=Student('Michael')
# s()

# # callable() 判断一个对象是否是可调用对象
# print(callable(Student('m')))
# print(callable(max))
# print(callable([1,2,3]))
# print(callable(None))
# print(callable('str'))

#枚举类
# JAN=1
# FEB=2
# MAR=3
# NOV=11
# DEC=12

# Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# # value 属性 是自动赋值给成员的 int 常量，默认是从1 开始计数。
# for name,member in Month.__members__.items():
#     print(name,'==>',member,',',member.value)

# print(Month.Jan.value)

# 保证没有重复值
# 自定义枚举值
# @unique
# class Weekday(Enum):
#     Sun=0
#     Mon=1
#     Tue=2
#     Wed=3
#     Thu=4
#     Fri=5
#     Sat=6
# day1=Weekday.Mon
# print(day1)
# print(day1.value)
# print(Weekday.Tue)
# print(Weekday['Wed'])
# print(Weekday(3))


# for name,member in Weekday.__members__.items():
#     print(name,'=>',member)

#使用元类__type()
# h=Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))

# 通过 type 创建 Hello 类
# def fn(self,name='World'):
#     print('Hello,%s'%name)
# Hello=type('Hello',(object,),dict(hello=fn)) #创建Hello class
# h=Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))


# 元类___metaclass
# metaclass是类的模板，所以必须以 type 类型派生
# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add']=lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)

# class MyList(list,metaclass=ListMetaclass):
#     pass

# l=MyList()
# l.add(1)
# l.add(2)
# print(l)
# __new__()方法接收到的参数依次是：
# 	1. 
# 当前准备创建的类的对象；
# 	2. 
# 类的名字；
# 	3. 
# 类继承的父类集合；
# 	4. 
# 类的方法集合。



# #ORM
# #定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)


class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s'%name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s==>%s'%(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings #保存属性和列的映射关系
        attrs['__table__']=name #假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s'%str(args))

class User(Model):
    #定义类的属性到列的映射
    id=IntegerField('id')
    name=StringField('name')
    email=StringField('email')
    password=StringField('password')

u=User(id=123,name='Michael',email='test@orm.com',password='pwd')
u.save()