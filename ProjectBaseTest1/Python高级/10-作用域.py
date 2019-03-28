# -*- coding: utf-8 -*-

#命名空间

#全局变量 局部变量
#globals locals


#LEGB 
#locals > enclosing function >globals >builtins
#locals 当前所在的命名空间(如函数、模块)，函数的参数也属于命名空间内的变量
#enclosing 外部嵌套函数的命名空间(闭包中常见)
#gloabls 全局变量，函数定义所在模块的命名空间
#builtins 内建模块，python 已经建好的
num=100
def test():
    #num=200
    def test2():
        #num=300
        print(num)
    return test2
ret=test()
ret()



