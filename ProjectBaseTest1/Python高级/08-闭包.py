# -*- coding: utf-8 -*-


#函数引用
# def test():
#     print('---1---')

# test() #执行函数
# print(test) #test  指向一个函数体
# b=test   #此时 b也指向这个函数体
# print(b)
# b() 



#闭包
# def test(number):
#     print('---1---')
#     def test_in(number_in):
#         print('---2---')
#         print('in test_in 函数,number is %d,number_in is %d'%(number,number_in))
#     print('---3---')   
#     return test_in

# ret=test(100)
# print(ret)
# ret(102)
# ret(105)
# ret(200)

#例子
def test(a,b):
    def test_in(x):
        print(a*x+b)
    return test_in
line1=test(1,1)
line1(0)
line2=test(5,4)
line2(0)
line1(0)



