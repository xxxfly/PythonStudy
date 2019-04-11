#-*- coding:utf-8 -*-
from functools import reduce

# 常用专有属性    说明    触发方式
# __init__	 构造初始化函数  创建实例后,赋值时使用,在 	__new__	 后
# __new__	 生成实例所需属性    创建实例时
# __class__	 实例所在的类   实例. 	__class__	
# 	__str__	 实例字符串表
# 示,可读性 print(类实例),如没实现,
# 使用repr结果
# 	__repr__	 实例字符串表
# 示,准确性 类实例	回⻋	或者
# print(repr(类实例))
# 	__del__	 析构 del删除实例
# 	__dict__	 实例自定义属
# 性 	vars(实例.__dict__)	
# 	__doc__	 类文档,子类不
# 继承 help(类或实例)
# 	__getattribute__	 属性访问拦截
# 器 访问实例属性时
# 	__bases__	 类的所有父类
# 构成元素 	 类名.__bases__	


# class Itcast(object):
#     def __init__(self,subject1):
#         self.subject1=subject1;
#         self.subject2='cpp'
#     #属性访问时拦截器
#     def __getattribute__(self,obj):
#         print('===1>%s'%obj)
#         if obj=='subject1':
#             print('log subject1')
#             return 'redirect python'
#         else:	#测试时注释掉这2行,将找不到subject2
#             temp=object.__getattribute__(self,obj)
#             print('===2>%s'%str(temp))
#             return temp
#     def show(self):
#         print('this is Itcast')

# s=Itcast('python')
# print(s.subject1)
# print(s.subject2)

# s.show()
# #1.先获取show属性对应的结果，应该是一个方法
# #2.方法()


#--------
#內建函数

#range函数 python2直接返回一个列表，python3 返回一个迭代值，需要的时候才返回一个值

#map函数
# map(function,sequence[,sequence,...])_->list
# function 是一个函数；sequence 是一个或多个序列，取决于function需要几个参数；返回一个list
l1=map(lambda x:x*x,[1,2,3,4,5])
for temp in l1:
    print(temp)
print('------')
l2=map(lambda x,y:x+y,[1,2,3],[4,5,6])
for temp in l2:
    print(temp)

#filter函数
#对指定的序列进行过滤操作
#filter(function or None,sequence) -> list,tump,or string
print('-------')
l3=filter(lambda x:x%2,[1,2,3,4,5]) 
for temp in l3:
    print(temp)

#reduce函数
#对参数序列中元素进行累积
#reduce(function,sequence[,initiall]) ->value
#function 有两个参数; sequence 序列可能str，tuple,list
#initial:固定初始值
print('------')
l4=reduce(lambda x,y:x+y,[1,2,3,4])
print(l4)

print('------')
l5=reduce(lambda x,y:x+y,[1,2,3,4],5)
print(l5)

print('------')
l6=reduce(lambda x,y:x+y,['aa','bb','cc'],'dd')
print(l6)

#sorted函数
#sorted(iterable,cmp=None,key=None,reverse=False) -->new
print('------')
l7=[22,11,2,3,452,44,34,56,24]
l7.sort()
print(l7)
l7.sort(reverse=True)
print(l7)
print(sorted(l7))
print(sorted(l7,reverse=1))