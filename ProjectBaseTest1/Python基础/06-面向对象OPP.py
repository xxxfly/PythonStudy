# -*- coding: utf-8 -*-
import types

#面向过程
# std1={'name':'Michael','score':98}
# std2={'name':'Bob','score':88}

# def print_score(std):
#     print('%s:%s'%(std['name'],std['score']))

# print_score(std1)

# #面向对象
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print('%s:%s'%(self.name,self.score))

# bart=Student('Bart Simpson',59)
# lisa=Student('Lisa Simpson',87)
# bart.print_score()
# lisa.print_score()

# #数据封装
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print('%s:%s'%(self.name,self.score))
#     def get_grade(self):
#         if self.score>=90:
#             return 'A'
#         elif self.score>=60:
#             return 'B'
#         else:
#             return 'C'
# zx=Student("zx",66)
# print(zx)
# print(Student)
# zx.name='zx1'
# print(zx.name)
# print(zx.get_grade())

# # 访问限制
# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name # 私有变量，只能内部可以访问，外部不能访问
#         self.__score=score # 私有变量，只能内部可以访问，外部不能访问
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_name(self,name):
#         self.__name=name
#     def set_score(self,score):
#         if 0<=score<=100:
#             self.__score=score
#         else:
#             raise ValueError('bad score')
#     def print_score(self):
#         print('%s:%s'%(self.__name,self.__score))
#     def get_grade(self):
#         if self.__score>=90:
#             return 'A'
#         elif self.__score>=60:
#             return 'B'
#         else:
#             return 'C'
    

# bart = Student('Bart Simpson', 59)
# print(bart.get_name())
# bart.set_score(89)
# print(bart.get_score())
# bart.name="zx"
# print(bart.get_name())
# print(bart.name)
# print(bart.get_grade())
# print(bart._Student__name) # 也可以访问 __name 变量，但是不要这样写


# #继承
# # 子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# class Tigger(Animal):
#     pass
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#     def eat(self):
#         print('Eating meat...')
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
# class Husky(Dog):
#     pass

# tigger=Tigger()
# tigger.run()
# dog=Dog()
# dog.run()
# dog.eat()
# cat=Cat()
# cat.run()
# husky=Husky()
# husky.run()
# husky.eat()


# # 多态
# a=list() #a是list类型
# b=Animal()#b是Animal类型
# c=Dog()#c是Dog类型

# print(isinstance(a,list))
# print(isinstance(b,Animal))
# print(isinstance(c,Dog))
# print(isinstance(c,Animal))

# # 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则
# def  run_twice(animal):
#     animal.run()
#     animal.run()
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())

# # 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了。
# class Timer(object):
#     def run(self):
#         print('Start...')

# run_twice(Timer())     


# # 获取对象信息
# # 判断对象类型 type

# a=Animal()
# d=Dog()
# print(type(123))
# print(type('sss'))
# print(type(None))
# print(type(abs))
# print(type(a))
# print(type(d))

# print(type('123')==type('abc'))
# print(type(a)==type(d))


# # 判断函数  需要导入 import types
# def fn():
#     pass
# print(type(fn))
# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x:x)==types.LambdaType)
# print(type(x for x in range(10))==types.GeneratorType)

# # isinstance 判断class 类型
# a=Animal()#a是Animal类型
# d=Dog()#d是Dog类型
# h=Husky()#h是Husky类型

# print(isinstance(h,Husky))
# print(isinstance(h,Dog))
# print(isinstance(h,Animal))

# print(isinstance(d,Dog) and isinstance(d,Animal))
# print(isinstance(d,Husky))

# print(isinstance('a',str))
# print(isinstance([1,2,3],(list,tuple)))
# print(isinstance((1,2,3),(list,tuple)))


# # dir 
# # dir(对象) 获取对象的所有属性和方法 ，返回包含字符串的list
# # len() __len__()
# print(dir('ABC'))
# print(len('ABC'))
# print('ABC'.__len__())

# class MyDog(object):
#     def __len__(self):
#         return 100

# dog=MyDog()
# print(len(dog))


# # 获取对象的状态信息
# # getattr() setattr() hasattr()
# class MyObject(object):
#     def __init__(self):
#         self.x=9
#     def power(self):
#         return self.x*self.x

# obj=MyObject()
# print(hasattr(obj,'x'))# 有属性'x'吗？
# print(obj.x)
# print(hasattr(obj,'y')) # 有属性'y'吗？
# setattr(obj,'y',19)# 设置一个属性'y'
# print(hasattr(obj,'y')) # 有属性'y'吗？
# print(getattr(obj,'y'))# 获取属性'y'
# #print(getattr(obj,'z'))# 获取属性'z'
# print(getattr(obj,'z',404))# 获取属性'z'，如果不存在，返回默认值404

# print(hasattr(obj,'power'))# 有属性'power'吗？
# fn=getattr(obj,'power')# 获取属性'power'并赋值到变量fn
# print(fn())

# def readImage(fp):
#     if hasattr(fp,'read'):
#         return readData(fp)
#     return None



# # 实例属性和类属性
# class Student1(object):
#     def __init__(self,name):
#         self.name=name

# s=Student1('Bob')
# s.score=90

# class Student(object):
#     name='student'
# s=Student() # 创建实例s
# print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# print(Student.name) # 打印类的name属性
# s.name='Michael'# 给实例绑定name属性
# print(s.name)# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问s
# del s.name # 如果删除实例的name属性
# print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


# #烤地瓜应用
# class CookPotato:
#     def __init__(self):
#         self.cookedString="生的"
#         self.cookedLevel=0
#         self.condiments=[]

#     def __str__(self):
#         return "地瓜的状态：%s(%d)，添加的%s"%(self.cookedString,self.cookedLevel,str(self.condiments))
#     def cook(self,cooked_time):
#         self.cookedLevel+=cooked_time
#         if self.cookedLevel>=0 and self.cookedLevel<3:
#             self.cookedString='生的'
#         elif self.cookedLevel>=3 and self.cookedLevel<5:
#             self.cookedString='半生不熟'
#         elif self.cookedLevel>=5 and self.cookedLevel<8:
#             self.cookedString='熟了'
#         elif self.cookedLevel>8 :
#             self.cookedString='烤糊了' 
#     def addCondiments(self,condimentStr):
#         self.condiments.append(condimentStr)   

# #创建一个地瓜对象
# digua=CookPotato()
# #开始烤地瓜
# digua.cook(1)
# print(digua)
# digua.cook(1)
# digua.addCondiments("酱")
# print(digua)
# digua.cook(1)
# print(digua)
# digua.addCondiments("辣椒粉")
# digua.cook(1)
# print(digua)
# digua.cook(1)
# digua.addCondiments("孜然")
# print(digua)
# digua.cook(1)
# print(digua)
# digua.cook(1)
# print(digua)
# digua.cook(1)
# print(digua)
# digua.addCondiments("芥末")
# digua.cook(1)
# print(digua)
# digua.cook(1)
# print(digua)



# #影藏对象的属性
# class Dog:
#     def set_age(self,new_age):
#         if new_age>0 and new_age<=30:
#             self.age=new_age
#         else:
#             self.age=0
#     def get_age(self):
#         return self.age
# dog=Dog()
# # dog.name="小白"
# # dog.age=3
# dog.set_age(10)
# print(dog.get_age())
# dog.set_age(100)
# print(dog.get_age())
# dog.age=3
# print(dog.get_age())


# #私有方法
# class Dog:
#     def __init__(self,new_name):
#         self.name=new_name
#         self._age=0 #私有属性

#     #私有方法
#     def __test1(self):
#         print('test1')
#     #共有方法
#     def test2(self):
#         print('test2')

# dog =Dog('小白')
# # dog.test1() # AttributeError: 'Dog' object has no attribute 'test1'
# dog.test2()


# #__del__方法 对象释放前会执行的方法
# class Dog:
#     def __init__(self):
#         self.age=0
#     def __del__(self):  #这个对象被释放之前一定会执行这个函数
#         print('----这个对象要被释放了------')

# dog1=Dog() #创建一个Dog对象   程序在结束之前也会将对象都给释放掉
# dog1.age=1
# print(dog1.age)
# dog2=dog1 #dog2 也指向 dog1 对象
# dog2.age=2
# print(dog1.age)
# print(dog2.age)
# del dog1
# print(dog2.age)
# del dog2
# print('===============')

#获取对象的引用计数的方式
#import sys
#sys.getrefcount(对象名) #返回的值比实际引用数大1，没有的话就会报错 

#----------------------------------
# #继承
# #父类
# class Animal:
#     def eat(self):
#         print('-----吃-----')
#     def drink(self):
#         print('-----喝-----')
#     def sleep(self):
#         print('-----睡觉-----')
#     def run(self):
#         print('-----跑-----')

# #继承类
# class Dog(Animal):
#     def bark(self):
#         print('----汪汪汪-----')

# class HaShiQi(Dog):
#     def fun(self):
#         print('-----犯二-----')
#     def bark(self):  #重写父类的方法
#         print('-----嗷叫-----')
#         #第一种掉用父类的方法
#         #Dog.bark(self) # 但是依然可以调用父类的方法
#         #第二种调用父类的方法
#         super().bark()

# # class Cat(Animal):
# #     def catch(self):
# #         print('----捉老鼠-----')
# # a=Animal()
# # a.eat()

# wangcai=Dog()
# wangcai.eat()
# wangcai.bark()

# erha=HaShiQi()
# erha.eat()
# erha.bark()
# erha.fun()
# # tom=Cat()
# # tom.eat()
# # tom.catch()


#---------------------------------------------------
# #私有方法、私有属性在继承的表现
# class A:
#     def __init__(self):
#         self.num1=100
#         self.__num2=200
#     def test1(self):
#         print('---test1---')
#     def __test2(self):
#         print('---test2---')
#     def test3(self):   #在父类中的共有方法是可以访问父类中的私有方法和私有属性
#         self.__test2()
#         print(self.__num2)
# class B(A):
#     def test4(self):
#         pass
#         # self.__test2()  #在 子类中 的共有方法是不能访问父类中的私有属性和私有方法
#         # print(self.__num2)

# b=B()
# b.test1()
# # b.__test2() #私有方法并不会被继承
# print(b.num1)
# # print(b.___num2)  #私有属性也不能被继承
# b.test3()  #正常访问
# # b.test4()  #异常

#-----------------------------------
# #多继承
# class Base(object):
#     def test(self):
#         print('---Base---')    
# class A(Base):
#     def test1(self):
#         print('---test1---')
# class B(Base):
#     def test2(self):
#         print('---test2---')
# #多继承，C即继承了A 也继承了B
# class C(A,B):  
#     pass

# c=C()
# c.test1() #可以调用A类中的test1方法
# c.test2() #也可以调用B类中的test2方法
# c.test()  #也可以调用Base类 的test方法
# #类名.__mro__ 返回的temp 顺序就是调用的父类 的顺序
# print(C.__mro__)



#------------------------------
# #多态
# class Dog(object):
#     def print_self(self):
#         print("大家好，我是xxx,....")

# class HaShiQi(Dog):
#     def print_self(self):
#         print("hello,everbody,")
# def introduce(temp):
#     temp.print_self()  #传递哪个对象，就调用哪个对象的方法

# dog1=Dog()
# dog2=HaShiQi()

# introduce(dog1)
# introduce(dog2) 

#---------------------
# #类属性，实例属性
# class Tool(object):
#     #属性
#     num=0 #类属性 属于类的
#     #方法
#     def __init__(self,new_name):
#         #实例属性
#         self.name=new_name  #实例属性 属于具体对象的，跟其他对象没有关系
#         #对类属性+1
#         Tool.num+=1

# tool1=Tool("铁锨")
# tool2=Tool("铲子")
# tool3=Tool("扫把")
# print(Tool.num)


#-------------------------------
# #类方法，实例方法，静态方法
# class Game(object):
#     #类属性
#     num=0

#     #实例方法
#     def __init__(self,new_name): #self接收当前实例
#         #实例属性
#         self.name=new_name
#         # #类属性
#         # Game.num+=1
#     #类方法
#     @classmethod
#     def add_num(cls): #接收类
#         cls.num+=1
    
#     #静态方法    
#     @staticmethod
#     def peint_menu():
#         print('-'*20)
#         print(' 穿越火线v1.0.0')
#         print(' 1.开始游戏')
#         print(' 2.退出游戏')
#         print('-'*20)



# game=Game('QQ飞车')
# Game.add_num()  #类方法可以通过类的名字调用
# game.add_num()  #还可以通过这个类创建出来的对象调用类方法
# print(Game.num)
# Game.peint_menu() #通过类来调用静态方法
# game.peint_menu() #也可以通过实例来调用静态方法


#-----------------------------
#4S店类
# class Store(object):
#     def select_car(self,car_type):
#         pass
#     def order(self,car_type):
#         return self.select_car(car_type)

# class BMWCarStore(Store):
#     def select_car(self,car_type):
#         return BMWFactory().select_car_by_type(car_type)

# class CarStore(Store):
#     def select_car(self,car_type):
#        return Factory().select_car_by_type(car_type)

# class BMWFactory(object):
#     def select_car_by_type(self,car_type):
#         pass

# class Factory(object):    
#     def select_car_by_type(self,car_type):
#         if car_type=='索纳塔':
#             return Suonata()
#         if car_type=='名图':
#             return Mingtu()
#         if car_type=='ix35':
#             return Ix35()

# class Car(object):
#     def move(self):
#         print("车在移动。。。")
#     def music(self):
#         print("车在播放音乐。。。")
#     def stop(self):
#         print("车在停止。。。")

# class Suonata(Car):
#     pass
# class Mingtu(Car):
#     pass
# class Ix35(Car):
#     pass

# car_store=CarStore()
# car=car_store.order("索纳塔")
# car.move()
# car.music()
# car.stop()


#---------------------------
# #__new__方法
# class Dog(object):
#     def __init__(self):
#         print('---init方法')
#     def __del__(self):
#         print('---del方法')
#     def __str__(self):
#         print('---str方法')
#         return '对象的描述信息'
#     def __new__(cls): #cls此时是Dog指向的那个对象
#         print(id(cls))  #这个ID跟 Dog类的一样
#         print('---new方法')
#         return object.__new__(cls)  #这个返回值表示创建处理对象的引用

# print(id(Dog))
# dog1=Dog()


#------------------------
# #单例模式---只有一个实例对象
# class Dog(object):
#     __instance=None  #定义类属性保存实例对象
#     __init_flag=False   
#     def __init__(self,name):
#         if Dog.__init_flag==False:
#             self.name=name
#             Dog.__init_flag=True
        
#     def __new__(cls,name):
#         if cls.__instance==None:  #如果是第一次创建实例对象，则返回新创建的实例对象
#             cls.__instance= object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance  #返回上次生成的实例对象


# # a=Dog()
# # b=Dog()
# # print(id(a))
# # print(id(b))

# a=Dog("旺财")
# print(id(a))
# print(a.name)
# b=Dog('二哈')
# print(id(b))
# print(b.name)




#---------------------------
#异常
# try:
#     print(num)
#     print('---1---')
# except NameError as identifier:  #错误类型
#     print("如果捕获到异常后的处理。。。")

# try:
#     open('123.txt')
#     print('---1---')
# except NameError as ex:
#      print(ex)
# except FileNotFoundError as identifier:
#     print('文件不存在')
# print('---2---')

# try:
#     open('123.txt')
#     print('---1---')
# except (NameError,FileNotFoundError) as ex:
#     print(ex)
#     print('文件不存在')
# except Exception:
#     print('如果用了Exception,那么意味着只要上面的except没有捕获到异常，那么这个except一定会捕获到')

# print('---2---')

# try:
#     #open('123.txt')
#     print('---1---')
# except (NameError,FileNotFoundError) as ex:
#     print(ex)
#     print('文件不存在')
# except Exception:
#     print('如果用了Exception,那么意味着只要上面的except没有捕获到异常，那么这个except一定会捕获到')
# else:
#     print('没有异常才会执行的地方')  
# print('---2---')

# try:
#     #open('123.txt')
#     print('---1---')
# except (NameError,FileNotFoundError) as ex:
#     print(ex)
#     print('文件不存在')
# except Exception:
#     print('如果用了Exception,那么意味着只要上面的except没有捕获到异常，那么这个except一定会捕获到')
# else:
#     print('没有异常才会执行的地方') 
# finally:
#     print('不管有没有异常，最终都会执行的地方') 
# print('---2---')


#----------------------
# #抛出自定义异常
# class ShortInputException(Exception):
#     '''自定义异常类'''
#     def __init__(self,length,atleast):
#         self.length=length
#         self.atleast=atleast
# def main():
#     try:
#         s=input('请输入-->')
#         if len(s)<3:
#             raise ShortInputException(len(s),3)
#     except ShortInputException as ex:
#         print('ShortInputException:输入的长度是%d，长度至少是%d'%(ex.length,ex.atleast))
#     else:
#         print('没有异常发生。')

# main()


#---------------------
# #异常处理抛出异常
# class Test(object):
#     def __init__(self,switch):
#         self.switch=switch
#     def calc(self,a,b):
#         try:
#             return a/b
#         except Exception as ex:
#             if self.switch==True:
#                 print('捕获异常')
#                 print(ex)
#             else:
#                 raise  #重新抛出这个异常，次数就不会被这个异常处理给捕获到，从而触发默认的异常处理

# test1=Test(True)
# test1.calc(11,0)

# test2=Test(False)
# test2.calc(11,0)



