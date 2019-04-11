#-*- coding:utf-8 -*-

class Test(object):
    def __init__(self,func):
        print('---初始化---')
        print('func name is %s'%func.__name__)
        self.__func=func
    def __call__(self):
        print('---装饰器中的功能---')
        self.__func()

# t=Test()
# t()  #如果不写__call__方法，是不能这样调用的

#_init__ __new__ __str__ __del__ __call__

@Test
def testFunc():
    print('---testFunc---')

testFunc()