# coding:utf-8


#pdb调试
#python3 -m pdb xxx.py
#l -->list显示当前的代码
#n -->next向下执行一行代码
#c -->continue继续执行程序
#b -->break 添加断点 b 行数
#clear --> 清除断点 clear 1 (第一个断点)
#s -->step 进入函数
#p --> print 打印一个变量的值 p result
#a --> 查看传入参数
#q --> 退出
#r --> return 快速执行函数的最后一行

def getAverage(a,b):
    result=a+b
    print('result=%d'%result)
    
    return result

a=100
b=200
c=a+b
ret=getAverage(a,b)
print(ret)