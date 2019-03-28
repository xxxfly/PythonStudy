#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random
import requests
import chardet
import psutil
#Pillow
#操作图像-缩放
#打开一个图片文件
# im=Image.open('File/test.png')
# #获取图像尺寸
# w,h=im.size
# print('Original image size:%s*%s'%(w,h))
# #缩放到50%
# im.thumbnail((w//2,h//2))
# print('Resize image to:%s*%s'%(w//2,h//2))
# #把缩放后的图像用png格式存储
# im.save('File/thumbnail.png','png')


#模糊
#打开一个图像文件
# im=Image.open('File/wx_20170614172855.jpg')
# #获取图像尺寸
# w,h=im.size
# print('Original image size:%s*%s'%(w,h))
# #应用模糊滤镜
# im2=im.filter(ImageFilter.BLUR)
# im2.save('File/blur.jpg','jpeg')

# #随机数字
# def rndChar():
#     return chr(random.randint(65,90))
# #随机颜色
# def rndColor():
#     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# #随机颜色2
# def rndColor2():
#     return (random.randint(32,255),random.randint(32,255),random.randint(32,255))

# #240*60
# width=60*4
# height=60
# image=Image.new('RGB',(width,height),(255,255,255))
# #创建Font对象
# font=ImageFont.truetype('Arial.ttf',36)
# #创建Draw对象
# draw=ImageDraw.Draw(image)
# #填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor())
# #输出文字
# for t in range(4):
#     draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# #模糊
# image=image.filter(ImageFilter.BLUR)
# image.save('code.jpg','jpeg')


#requests
# r=requests.get('https://www.baidu.com/') #百度首页
# print(r.status_code)
# print(r.text)

# r=requests.get('https://www.baidu.com/s',params={'wd':'python','rsv_spt':'1'})
# print(r.url)
# print(r.encoding)
# print(r.content)
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())


# r=requests.get('https://www.baidu.com/',headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'})
# print(r.text)

# r=requests.post('http://localhost:6234/cdn/Home/_Login_.aspx',data={'txtAccount':'admin','txtPassword':'123456'})
# print(r.url)
# print(r.text)

# params={'key','value'}
# r=requests.post('url',json=params) #内部自动序列化为JSON

# upload_files={'file':open('File/test01.txt','rb')}
# r=requests.post('url',files=upload_files) 

# r.headers #获取头部信息 {'':''}
# r.cookies['cookiename']  #获取cookie信息，''
# r=requests.get('url',cookies={'token':'123','status':'1'}) #添加cookie 信息
# r=requests.get('url',timeout=3) #3秒后超时


#chardet
# print(chardet.detect(b'Hello,world!'))

# data='清明时节雨纷纷，路上行人欲断魂'.encode('gbk')
# print(chardet.detect(data))
# data='清明时节雨纷纷，路上行人欲断魂'.encode('utf-8')
# print(chardet.detect(data))
# data='最新の主要ニュース'.encode('euc-jp')
# print(chardet.detect(data))


#psutil
# print(psutil.cpu_count()) #CPU逻辑数量
# print(psutil.cpu_count(logical=False)) #CPU物理核心

# print(psutil.cpu_times())#获取CPU的用户/系统/空闲时间
# #CPU使用率，每秒刷新一次，累计10次
# for x in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))

# print(psutil.virtual_memory()) #获取物理内存信息
# print(psutil.swap_memory()) #获取交换内存信息

# print(psutil.disk_partitions()) #磁盘分区信息
# print(psutil.disk_usage('E:\\')) #磁盘的使用情况
# print(psutil.disk_io_counters()) #磁盘IO


# print(psutil.net_io_counters()) #获取网络读写字节/包的个数
# print(psutil.net_if_addrs()) #获取网络接口信息
# print(psutil.net_if_stats()) #获取网络接口状态
# #print(psutil.net_connections()) #获取当前网络的连接信息

# #print(psutil.pids()) #所有进程ID
# p=psutil.Process(7768)
# print('进程名称:',p.name()) #进程名称
# print('进程路径:',p.exe()) #进程路径
# print('进程工作目录:',p.cwd()) #进程工作目录
# print('进程启动命令:',p.cmdline()) #进程启动命令
# print('父进程ID:',p.ppid()) #父进程ID
# print('父进程:',p.parent()) #父进程
# print('子进程列表:',p.children()) #子进程列表
# print('进程状态:',p.status()) #子进程状态
# print('进程用户名:',p.username()) #进程用户名
# print('进程创建时间:',p.create_time()) #进程创建时间
# #print('进程终端:',p.terminal()) #进程终端
# print('进程使用CPU时间:',p.cpu_times()) #进程使用CPU时间
# print('进程使用的内存:',p.memory_info()) #进程使用的内存
# print('进程打开的文件:',p.open_files()) #进程打开的文件
# print('进程相关的网络连接:',p.connections()) #进程相关的网络连接
# print('进程的线程数量:',p.num_threads()) #进程的线程数量
# print('所有线程信息:',p.threads()) #所有线程信息
# print('进程的环境变量:',p.environ()) #进程的环境变量
# #print('结束进程:',p.terminate()) #结束进程


# psutil.test()