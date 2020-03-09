

res=[]
for x in 'spam':
    res.append(ord(x))

print(res)

print(list(map(ord,'spam')))
print([ord(x) for x in 'spam'])

# 列表解析
print([x**2 for x in range(10)])

print(list(map((lambda x:x**2),range(10))))

# 列表解析
print([x for x in range(10) if x%2==0])

print(list(filter(lambda x:x%2==0,range(10))))

print(open('mytext.txt').readlines())

print([line.rstrip() for line in open('mytext.txt').readlines()])

# 生成器函数
def gensquares(n):
    for i in range(n):
        y=yield i**2
        print(y)
    
g=gensquares(5)
next(g)
g.send(88)
next(g)
g.send(77)
next(g)

# 生成器表达式
g=(x**2 for x in range(10))


def mymap(func,*seqs):
    res=[]
    for args in zip(*seqs):
        res.append(func(*args))
    return res

print(mymap(abs,[-2,-1,0,1,4,5]))
print(mymap(pow,[1,2,3],[1,2,3,4,5]))

# 列表解析
def mymap2(func,*seqs):
    return [func(*args) for args in zip(*seqs)]

print(mymap2(abs,[-2,-1,0,1,4,5]))
print(mymap2(pow,[1,2,3],[1,2,3,4,5]))

# 生成式
def mymap3(func,*seqs):
    for args in zip(*seqs):
        yield func(*args)

print(list(mymap3(abs,[-1,-2,0,2,1])))   


def mymap4(func,*seqs):
    return (func(*args) for args in zip(*seqs))

print(list(mymap4(abs,[-1,-2,0,2,1])))   

def myzip(*seqs):
    minlen=min(len(s) for s in seqs)
    return (tuple(seq[i] for seq in seqs) for i in range(minlen))

print(list(myzip('abc','12345')))


def myzip2(*seqs):
    iters=list(map(iter,seqs))
    while iters:
        res=[next(i) for i in iters]
        yield tuple(res)
    
print(list(myzip2('abc','12345')))

# import string
# from . import string