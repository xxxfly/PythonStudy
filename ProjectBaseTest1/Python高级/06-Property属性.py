# -*- coding: utf-8 -*-

class Test(object):
    def __init__(self):
        self.__num=100
    def setNum(self,newNum):
        print('----setter----')
        self.__num=newNum
    def getNum(self):
        print('----getter----')
        return self.__num

    num=property(getNum,setNum)

t=Test()
print(t.getNum())
t.setNum(50)
print(t.getNum())

print('*'*50)
t.num=200  #相当于调用了 t.setNum(200)
print(t.num) #相当于调用了 t.getNum()


class Money(object):
    def __init__(self):
        self.__money=100
    @property
    def money(self):
        print('---getter---')
        return self.__money
    @money.setter
    def money(self,newValue):
        print('---setter---')
        self.__money=newValue       

mon=Money()
mon.money=200
print(mon.money)

    