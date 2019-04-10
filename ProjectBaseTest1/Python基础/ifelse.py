#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from enum import Enum, unique
import os

# age=int(input('请输入年龄:'))
# if age>=18:
#     print('you age is',age)
#     print('adult')
# elif age>=6:
#     print('you age is',age)
#     print('teenager')
# else:
#     print('you age is %d'%(age))
#     print('kid')
# x='1'
# if x:
#     print('True')

# height=float(input('请输入身高(m)：'))
# weight=float(input('请输入体重(kg)：'))
# bmiValue=weight/(height*height)

# if bmiValue<=18.5:
#     print('您的BMI值是 %.2f,过轻'%(bmiValue))
# elif bmiValue<=25:
#     print('您的BMI值是 %.2f,正常'%(bmiValue))
# elif bmiValue<=28:
#     print('您的BMI值是 %.2f,过重'%(bmiValue))
# elif bmiValue<=32:
#     print('您的BMI值是 %.2f,肥胖'%(bmiValue))
# else:
#     print('您的BMI值是 %.2f,严重肥胖'%(bmiValue))

# #变量
# #变量的类型
# num1=100 #num1就是一个变量
# num2=87 #num2也是一个变量
# total=num1+num1

# applePrice=3.5 #苹果的价格 元/斤
# weight=7.5 #购买的苹果的种类 斤
# money=applePrice*weight #需支付的价格 第一次出现是定义变量
# money=money-10 #第二次就出现不是定义变量，而是给这个变量赋上新的值


# # height=input("请输入你的身高：")
# height=190
# print('你的身高是 %d cm' %height)
# name="zx"
# print("名字是：%s"%name)

# #1.使用input 获取必要的信息
# name=input("请输入名字：")
# QQ=input("请输入QQ：")
# #2.使用print来打印名片
# print("="*15)
# print("姓名：%s"%name)
# print("QQ：%s"%QQ)
# print("="*15)

# 使用print输出多个变量
# name="zx"
# age=23
# addr="信阳"
# print("姓名：%s,年龄:%d,地址：%s"%(name,age,addr))


# age =19
# #比较运算符
# if age >=18:
#     print("成年人。。。")
# else:
#     print("未成年人。。。")


# #逻辑运算符
# if 1 or 2:
#     pass
# if 1 and 2:
#     pass
# number=0
# if not (number>0):
#     pass

# if number>0 and number<20:
#     pass
# elif number>20:
#     pass
# else:
#     pass

# if elif else
# num=int(input("请输入今天日期："))
# if num==1:
#     print("今天星期一")
# elif num==2:
#     print("今天星期二")
# elif num==3:
#     print("今天星期三")
# elif num==4:
#     print("今天星期四")
# elif num==5:
#     print("今天星期五")
# elif num==6:
#     print("今天星期六")
# elif num==7:
#     print("今天星期天")
# else:
#     print("输入有误")


# while 循环  *三角
# num=1
# while num<=5:
#     j=1
#     while j<=num:
#         print("*",end="")
#         j+=1
#     print("")
#     num+=1

# while *倒三角
# num=1
# while num<=5:
#     j=5
#     while j>=num:
#         print("*",end="")
#         j-=1
#     print("")
#     num+=1

# 99乘法表
# i=1
# while i<=9:
#     j=1;
#     while j<=i:
#         print('%d*%d=%d\t'%(j,i,j*i),end="")
#         j+=1
#     print("")
#     i+=1


# #1.提示并获取用户的输入
# player=int(input("请输入:剪刀0 石头1 布2:"))
# #让电脑出一个
# computer=random.randint(0,2)
# print("您输入的是%s,电脑输入的是%s"%(player,computer))
# #2.判断用户的输入，然后显示对应的结果
# if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
#     print("赢了")
# elif player==computer:
#     print("平局了")
# else:
#     print("输了")


# 打印1-100之间的偶数
# i=1
# count=0
# while i<=100:
#     if i%2==0:
#         print(i)
#         count+=1
#     if count==20:
#         break

#     i+=1

# #数组 添加 append()  insert(位置,元素) extend()
# names=["张三","李四","王五"]
# names.append("赵六")
# print(names)
# names.insert(1,"小明")
# print(names)
# names.insert(3,"小红")
# print(names)

# names2=["悟空","八戒","沙僧"]
# print(names2)

# print(names+names2)

# names.extend(names2)
# print(names)


# 数组 -删除  pop() remove("元素") 只删除一次     del list[] 根据下标删除
# names.pop()
# print(names)
# names.pop()
# print(names)
# names.remove("李四")
# print(names)

# print(names[0])
# print(names[1])
# print(names[1:3])

# del names[1]
# print(names)

# #修改
# names[0]="张三说"
# print(names)

# #查询 in /  not in
# if "李四" in names:
#     print("找到了")

# 名片管理系统
# 1.打印功能提示
# print("*"*50)
# print(" 名片管理系统 v1.0")
# print(" 1:添加一个新的名片")
# print(" 2:删除一个名片")
# print(" 3:修改一个名片")
# print(" 4:查询一个名片")
# print(" 5:显示名片信息")
# print(" 6:退出")
# print("*"*50)
# cards=[] #定义列表用来存储 名片信息 列表
# while True:
#     #2.获取用户输入
#     num=int(input("请输入操作序号:"))
#     #3.根据用户的输入进行相应的功能
#     if num==1:

#         new_name=input("请输入名字:")
#         new_age=int(input("请输入年龄:"))
#         new_addr=input("请输入地址:")
#         new_QQ=input("请输入QQ:")

#         #定义一个新的字典，用来存储名片信息
#         new_card={}
#         new_card['name']=new_name
#         new_card['age']=new_age
#         new_card['addr']=new_addr
#         new_card['QQ']=new_QQ
#         #将一个字典添加到列表中
#         cards.append(new_card)
#         print(cards)
#     elif num==2:
#         remove_name=input("请输入要删除的名字:")
#         #遍历列表，找到要删除的名字是属于列表中哪个字典的
#         for card in cards:
#             if card.get('name')==remove_name:
#                 cards.remove(card)
#         print(cards)
#     elif num==3:
#         update_name=input("请输入要修改的名字:")
#         new_name=input("请输入修改后的名字:")
#         #遍历名片列表，查出来之后验证是哪个名片后，直接修改属性值
#         for index in range(len(cards)):
#             if cards[index].get('name')==update_name:
#                 cards[index]['name']=new_name
#         print(cards)
#     elif num==4:
#         find_name=input("请输入要查询的名字:")
#         for card in cards:
#             if card.get('name')==find_name:
#                 print("找到了 %s"%find_name)
#                 break
#         else:
#             print("查无此人。。。")
#     elif num==5:
#         print("%s\t%s\t%s\t%s"%("姓名","年龄","地址","QQ"))
#         for card in cards:
#             print("%s\t%s\t%s\t%s"%(card['name'],card['age'],card['addr'],card['QQ']))
#     elif num==6:
#         print("再见")
#         break
#     else:
#         print("您的输入有误，请重新输入")
#     print("")


# 字典
# student={'name':'张三','age':18,'addr':'河南'}
# print(student)
# student['QQ']='123456789'
# print(student)
# student['QQ']=123456
# print(student)
# del student['QQ']
# print(student)
# print(student.get("QQ"))
# print(student.get("name"))


# nums=[11,22,33,44,55]
# for temp in nums:
#     print(temp)
# else:
#     print("======")

# #append--extend
# nums1=[11,22,33]
# nums2=[44,55]

# #nums1.extend(nums2)
# nums1.append(nums2)
# print(nums1)

# 元祖---不允许修改(增、删、改都不行)，只能查看(只读)
# nums=(11,22,33)
# print(type(nums))
# a,b,c=nums
# print(a,b,c)

# #字典-字典的操作
# student={'name':'张三','age':19,'addr':'河南'}
# print(len(student))
# print(student.keys())
# print(student.get("name"))
# print(student.get("aa"))
# if "qq" in student.keys():
#     print("有这个键")
# print(student.values())

# for temp in student.keys():
#     print(temp)
# for temp in student.values():
#     print(temp)
# for temp in student.items():
#     print(temp)
# for temp in student.items():
#     print("key=%s,value=%s"%(temp[0],temp[1]) )

# for key,value in student.items():
#     print('%s:%s'%(key,value))

# def sumNum(a,b):
#     sum=a+b
#     return sum

# num1=int(input("请输入数字1:"))
# num2=int(input("请输入数字2:"))

# print("%d+%d=%d"%(num1,num2,sumNum(num1,num2)))

# def sum_3_nums(a,b,c):
#     sumResult=a+b+c
#     #print("%d+%d+%d=%d"%(a,b,c,sumResult))
#     return sumResult

# def average_3_nums(a,b,c):
#     sumResult=sum_3_nums(a,b,c)
#     avgResult=sumResult/3
#     return avgResult

# result=average_3_nums(1,2,3)
# print(result)

# #全局变量
# b=100

# #局部变量
# def test1():
#     a=100 #局部变量
#     print("a=%d"%a)
#     print("b=%d"%b) #全局变量

# def test2():
#     a=100 #局部变量

# test1()
# test2()

# #定义全局变量
# g_temperature=0
# def get_temperature():
#     #如果temperature这个变量已经在全局变量的位置定义了，此时还想在函数中对这个全局变量进行修改的话，那么，仅仅是 temperature=一个值 是不够的，
#     #此时这个temperature 这个变量仅仅是一个局部变量，和 全局变量的名字相同而已
#     #使用gloabl 用来对一个全局变量的声明，那么这个函数中的 temperature=23 就不是定义一个局部变量，而是对全局变量的值进行修改
#     global g_temperature
#     g_temperature=23

# def print_temperature():
#     print("温度是%d"%g_temperature)
# get_temperature()
# print_temperature()


# #学生管理系统
# #定义全局变量 数组用来存储名片信息
# card_infos=[]
# #打印系统菜单
# def print_menu():
#     """完成打印功能菜单"""
#     print("="*50)
#     print(" 名片管理系统 V0.01")
#     print("1.添加一个新的名片")
#     print("2.删除一个名片")
#     print("3.修改一个名片")
#     print("4.查询一个名片")
#     print("5.显示所有的名片")
#     print("6.退出")
#     print("="*50)

# #新增一个名片
# def add_new_card_info():
#     '''完成新增一个名片'''
#     new_name=input("请输入新的名字:")
#     new_qq=input("请输入新的QQ:")
#     new_weixin=input("请输入新的微信:")
#     new_addr=input("请输入新的住址:")

#     #定义一个字典，用来存储一个新的名片
#     new_info={}
#     new_info['name']=new_name
#     new_info['qq']=new_qq
#     new_info['weixin']=new_weixin
#     new_info['addr']=new_addr

#     #讲一个字典添加到列表中
#     global card_infos
#     card_infos.append(new_info)


# print_menu()

# while True:

#     num=int(input("请输入操作编号："))

#     if num==1:
#         pass
#     elif num==2:
#         pass
#     elif num==3:
#         pass
#     elif num==4:
#         pass
#     elif num==5:
#         pass
#     elif num==6:
#         print("再见")
#         break
#     else:
#         print("输入有误，请重新输入")

#     print("")


# 参数
# 不定长参数
# def sum_nums(a,b,c=33,*args,**kw):
#     print("-"*30)
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kw)
#     result=a+b
#     for item in args:
#         result+=item
#     #print(result)

# sum_nums(3,2,66,43,45)
# sum_nums(3,2,66)
# sum_nums(3,2,22,66,88,task=99,done=89)
# A=(22,21,20)
# B={'name':'zx','age':19}
# sum_nums(3,2,66,*A,**B)


# #递归

# def test(num):
#     print("num=%d"%num)
#     if num==1:
#         return 1
#     return num*test(num-1)

# print(test(5))

# #尾递归
# def fact(num):
#     return fact_item(num,1)
# def fact_item(num,product):
#     if num==1:
#         return 1
#     return fact_item(num-1,num*product)

# print(fact(10))


# # 匿名函数
# lambda x, y: x+y

# nums = [11, 22, 1, 2234, 123, 23, 45, 3, 2, 5]
# nums.sort()
# print(nums)

# infos = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 28}, {
#     'name': 'wangwu', 'age': 20}, {'name': 'zhaoliu', 'age': 19}]

# infos.sort(key=lambda x: x['name'])
# print(infos)

# infos.sort(key=lambda x: x['age'])
# print(infos)


# a=[100]
# def test(num):
#     #num+=num   #输出 [100,100] [100,100]
#     num=num+num #输出 [100,100] [100]
#     print(num)

# test(a)
# print(a)


#字符串操作


# f=open("File/test.txt",'w',encoding='utf-8')  #r读 w写 a追加
# f.write("测试")
# f.close()

#文件复制
# f_oig=open("File/test.txt",'r',encoding='utf-8')
# f_new=open("File/test[复件].txt",'w',encoding='utf-8')
# f_new.write(f_oig.read())
# f_new.close()
# f_oig.close()

# #文件读取 readlines   返回每行数据的总列表
# f=open('File/test.txt','r',encoding='utf-8')
# print(f.readlines())
# f.close()


# #文件读取 readline   返回每行的数据
# f=open('File/test.txt','r',encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# #读取大文件 
# f_read=open('File/test.txt','r',encoding='utf-8')
# f_writer=open('File/test[复制].txt','w',encoding='utf-8')
# while True:
#     content=f_read.read(1024)  #按大小分片取
#     if len(content)==0:
#         break
#     f_writer.write(content)
# f_read.close()
# f_writer.close()

# #文件操作 定位
# f=open('File/test.txt','r+',encoding='utf-8')
# print('位置：%s'%f.tell())
# print(f.read(1))
# print(f.read(1))
# print(f.read(1))
# print(f.read(1))
# print(f.read(1))
# print('位置：%s'%f.tell())
# f.seek(0,2)
# print(f.read(1))
# print('位置：%s'%f.tell())
# f.seek(6,0)
# print(f.read(1))
# print(f.read(1))
# f.close()


#文件操作 更改名字
# os.rename('File/test.txt','File/test1.txt')  #重命名
# os.remove('File/test.txt') #删除文件
# os.mkdir('haha')  #创建文件夹
# os.getcwd() #获取当前路径
# os.chdir('haha') #改变当前路径
# os.listdir('./')  #获取目录列表
# os.rmdir('haha/') #删除目录

#文件批量操作
# os.mkdir('haha')
os.chdir('haha')
print(os.getcwd())

print(os.listdir('./'))
fileList=os.listdir('.')
for item in fileList:

    #filename='test'+str(i)+'.txt'
    filename=item
    index=filename.rindex('.')
    new_filename=filename[0:index]+'测试'+filename[-(len(filename)-index):]
    os.rename(filename,new_filename)
    # f=open(filename,'w')
    # f.close()


    







