#-*- coding:utf-8 -*-

#元类
# # --类也是对象，就是一组用来描述如何生成一个对象的代码段
# class Person(object):
#     num=0
#     print('--person--test--')  #会直接被执行，说明此时python解释器已经创建了这个类
#     def __init__(self):
#         self.name='a'

# print(100)
# print('hello')
# print(Person)


# class Person():
#     pass
# p1=Person()
# print(type(p1))


#---------------------------------------
# #type 创建类type(类名，集成，方法和属性)
# Test2=type('Test2',(),{'name':'a'})
# t2=Test2()
# print(t2.name)
# print(type(t2))


# def printNum(self):
#     print('--num:%d'%self.num)

# Test3=type('Test3',(),{'printNum':printNum,'num':100})

# t3=Test3()
# t3.printNum()



#__metaclass__  