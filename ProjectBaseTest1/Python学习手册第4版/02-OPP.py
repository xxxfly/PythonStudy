
class c1(object):
    """
    •class语句创建类对象并将其赋值给变量名。
    •class语句内的赋值语句会创建类的属性。
    •类属性提供对象的状态和行为。

    """
    x=1
    y=2
    print('c1')

print('start')
#•像函数那样调用类对象会创建新的实例对象。
#•每个实例对象继承类的属性并获得了自己的命名空间。
#•在方法内对self属性做赋值运算会产生每个实例自己的属性。
c1i1=c1()
print(c1i1.x)


class FirstClass(object):
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)

x=FirstClass()
y=FirstClass()

x.setdata('xxx')
y.setdata(3.1415)

x.display()
y.display()

x.data='xxxx2'
x.display()

class SecondClass(FirstClass):
    def display(self):
        print('Current value="%s"'%self.data)
    
s1=SecondClass()
s1.data='s1'
s1.display()


class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value
    def __add__(self,other):
        return ThirdClass(self.data+other)
    def __str__(self):
        return '[ThirdClass:%s]'%self.data
    def mul(self,other):
        self.data*=other

t1=ThirdClass('abc')
t1.display()
print(t1)

t2=t1+'xyz'
t2.display()
print(t2)

t1.mul(3)
print(t1)


print('*'*30)
# 类对象属性和实例对象属性
class MixedName:
    data = 'spam'
    def __init__(self,value):
        self.data = value
    def display(self):
        print(self.data, MixedName.data)
    

print(MixedName.data)
mn1 = MixedName(1)
mn2 = MixedName(2)
mn1.display()
mn2.display()
MixedName.display(mn1)
MixedName.display(mn2)