# -*- coding: utf-8 -*-
import json

# #outer是外部函数 a和b都是外函数的临时变量
# def ourter(a):
#     b=10
#     #inner是内函数
#     def inner():
#         #在内函数中 用到了外函数的临时变量
#         print(a+b)
#     #外函数的返回值是内函数的引用
#     return inner

# if __name__=="__main__":
#     #我们调用外部函数 传入参数5
#     #此时外函数的两个临时变量 a是5 b是10，并创建了内函数，然后把内函数的引用返回存给了 demo
#     #外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数。
#     demo=ourter(5)
#     #我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
#     #demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
#     demo()
#     demo2=ourter(7)
#     demo2()


#=============================

# #修改闭包变量的实例
# #ourter是外部函数， a和b都是外函数的临时变量
# def ourter(a):
#     b=10 # a和b都是闭包变量
#     c=[a] #这里对应修改闭包变量的方法2
#     #inner是内函数
#     def inner():
#         #内函数中想修改闭包变量
#         #方法1 nonlocal 关键字声明
#         nonlocal b
#         b+=1
#         # 方法2，把闭包变量修改成可变数据类型，比如列表
#         c[0]+=1
#         print(c[0])
#         print(b)
#     #外函数的返回值是内函数的引用
#     return inner

# if __name__=='__main__':

#     demo=ourter(5)
#     demo()


#=============================

# def ourter(x):
#     def inner(y):
#         nonlocal x
#         x+=y
#         return x
#     return inner

# a=ourter(10)
# print(a(2))
# print(a(3))

#=============================

# def create():
#     return [lambda x:i*x for i in range(5)]
# print(create())
# for mul in create():
#     print(mul(2))

# def create2():
#     return [lambda x,i=i:i*x for i in range(5)]
# print(create2())
# for mul in create2():
#     print(mul(2))


str1= '{"result":{"status":{"code":0,"msg":"success"},"timestamp":"Thu May 03 15:17:08 +0800 2018","data":[{"loc_code":"4a-41-58-58-30-30-38-35","url":"tokyo","eng_name":"Tokyo","chinese_name":"东京","is_capital":"1","is_important":"0"},{"loc_code":"4a-41-57-41-30-31-36-37","url":"yokohama","eng_name":"Yokohama","chinese_name":"横滨","is_capital":"0","is_important":"1"},{"loc_code":"4a-41-58-58-30-33-32-39","url":"osakashi","eng_name":"Osaka-shi","chinese_name":"大阪市","is_capital":"0","is_important":"0"},{"loc_code":"4a-41-58-58-30-30-37-31","url":"osaka","eng_name":"Osaka","chinese_name":"大阪","is_capital":"0","is_important":"1"},{"loc_code":"4a-41-58-58-30-32-39-33","url":"nagoyashi","eng_name":"Nagoya-shi","chinese_name":"名古屋市","is_capital":"0","is_important":"0"},{"loc_code":"4a-41-58-58-30-30-35-37","url":"nagoya","eng_name":"Nagoya","chinese_name":"名古屋","is_capital":"0","is_important":"1"},{"loc_code":"4a-41-58-58-30-33-34-32","url":"sapporoshi","eng_name":"Sapporo-shi","chinese_name":"札幌市","is_capital":"0","is_important":"0"},{"loc_code":"4a-41-58-58-30-30-37-38","url":"sapporo","eng_name":"Sapporo","chinese_name":"札幌","is_capital":"0","is_important":"1"},{"loc_code":"4a-41-58-58-30-32-33-37","url":"kobeshi","eng_name":"Kobe-shi","chinese_name":"神户市","is_capital":"0","is_important":"0"},{"loc_code":"4a-41-58-58-30-30-34-30","url":"kobe","eng_name":"Kobe","chinese_name":"神户","is_capital":"0","is_important":"1"},{"loc_code":"4a-41-58-58-30-31-34-36","url":"fukuokashi","eng_name":"Fukuoka-shi","chinese_name":"福冈市","is_capital":"0","is_important":"1"},{"loc_code":"4a-41-58-58-30-30-34-37","url":"kyoto","eng_name":"Kyoto","chinese_name":"京都","is_capital":"0","is_important":"1"}]}}'

json111=json.loads(str1)

print(json111)