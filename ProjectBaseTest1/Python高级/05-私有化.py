# -*- coding: utf-8 -*-

#私有化
class Test(object):
    def __init__(self):
        self.__num=100   #__属性名，就是私有属性，实例对象直接使用不能使用
    def setNum(self,newNum):
        self.__num=newNum
    def getNum(self):
        return self.__num
    
t=Test()
#print(t.__num)  #会提示找不到这个属性
#t.__num=200  #此时是对实例属性新增一个属性 __num  不是类里面的__num
t.setNum(200)
print(t.getNum())

#xxx   公有变量
# __xxx 私有属性 只有类自己可以用，无法在外部直接访问
# _xxx  from module import * 禁止导入，类对象和子类可以访问
#__xxx__ 用户名字空间的魔法对象或属性
#xxx_  避免与python关键字冲突