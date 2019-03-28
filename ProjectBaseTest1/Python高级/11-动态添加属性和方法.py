# -*- coding: utf-8 -*-
import types
class Person(object):
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge
    def eat(self):
        print('正在吃')
        
def run(self):
    print('--%s正在跑--'%(self.name))   
xiaoli=Person('小李',23)
print(xiaoli.name)
print(xiaoli.age)
xiaoli.addr='cszc'
print(xiaoli.addr)

Person.num=100
print(xiaoli.num)

xiaoli.eat()
# xiaoli.run=run(xiaoli) #
# xiaoli.run()

xiaoli.run=types.MethodType(run,xiaoli) #将方法绑定到对象上面
#xiaoli.run()
