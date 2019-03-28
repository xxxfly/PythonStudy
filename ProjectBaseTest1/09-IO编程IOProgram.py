# -*- coding: utf-8 -*-
import io
from io import StringIO
from io import BytesIO
import os
import pickle
import json

#文件读
# try:
#     f=open('File/test01.txt','r',encoding='utf-8')
#     print(f.read())
# finally:
#     f.close()

# f.read(size) 每次最多读取size 个字节的内容
# with open('File/test01.txt','r',encoding='utf-8') as f:
#     # print(f.read(8))
#     # print(f.read(8))
#     # print(f.read(8))
#     # print(f.read(8))
#     while True:
#         s=f.read(8)
#         if not s:
#             break
#         print(s)

# f.readlines() 一次读取所有行内容并返回list
# with open('File/test01.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line.strip())

# StringIO
# 把 str 写入StringIO
# f=StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.write('python'))
# print(f.getvalue())

# 读取str
# f=StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.strip())


# BytesIO
# 操作二进制数据
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

# f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())


#操作文件和目录
# print(os.name)
# print(os.environ) #环境变量
# print(os.environ.get('PATH','default'))

# print(os.path.abspath('.'))#查看当前目录的绝对路径
# print(os.path.join(os.path.abspath('.'),'test'))#在某个目录下创建一个新目录，首先得把新目录的完整路径表示出来
# # os.mkdir(os.path.join(os.path.abspath('.'),'test'))#创建一个目录
# # os.rmdir(os.path.join(os.path.abspath('.'),'test'))#删除一个目录

# print(os.path.split(os.path.join(os.path.abspath('.'),'test')))

# print(os.path.splitext('E:\zx\PythonProject\ProjectTest2\test\file.txt'))
# os.rename('test.txt','File/test01.txt') #对文件重新命名
# os.remove('File/test01.txt') #删除文件

# 序列化 import pickle
# 把变量从内测中变为可存储或传输的过程称之为序列化
# 把变量内容从序列化的对象重新读到内存里称之为反序列化
# d=dict(name='Bob',age=20,score=80)
# print(pickle.dumps(d))

# 直接把对象序列化后写入一个 file-like Object 
# f=open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

# 把内容读到一个 Bytes,然后用 pickle.loads() 方法反序列化出对象。也可以直接用 pickle.load() 从一个 file-like Object 中直接反序列化出对象
# f=open('dump.txt','rb')
# d=pickle.load(f)
# f.close()
# print(d)


# json
# d=dict(name='Bob',age=20,score=80)
# print(json.dumps(d))
# print(isinstance(json.dumps(d),str))
# json_str='{"age":20,"score":80,"name":"Bob"}'
# print(json.loads(json_str))


#json进阶
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',20,80)

def student2dic(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print(json.dumps(s,default=student2dic))
print(s.__dict__)
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str='{"age":20,"score":80,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))

