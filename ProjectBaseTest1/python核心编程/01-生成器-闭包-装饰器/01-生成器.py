#encoding=utf-8

#列表生产式，但是受内存现在，不能无限大
a=[x*2 for x in range(10)]
print(a)


#生成器，只是保持生成的方法，只是需要的时候才生成
b=(x*2 for x in range(10))
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
#print(next(b))   #超出内容长度 则会抛出错误

#创建生成器方法2--yield
def fib(times):
    print('---start---')
    n=0
    a,b=0,1
    for i in range(times):
        print('---1---') 
        yield b    #执行next()的时候，遇到yield 就停止，并把yeild 后面的值返回，还记住停止的位置，等下次在执行next()的时候开始从停止的地方后面开始执行
        print('---2---')
        a,b=b,a+b
        n+=1
    print('---stop---')
f=fib(5)  #f 此时是生成器对象
print(f)
print(next(f))
print(next(f))
print(next(f))




    