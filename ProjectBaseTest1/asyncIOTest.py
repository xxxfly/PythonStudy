#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading
from aiohttp import web

# loop=get_event_loop()
# while True:
#     event=loop.get_event()
#     process_event(event)

# def A():
#     print('1')
#     print('2')
#     print('3')

# def B():
#     print('A')
#     print('B')
#     print('C')

# A()
# B()

#协程
# def consumer():
#     r=''
#     while True:
#         n=yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r='200 OK'
# def produce(c):
#     c.send(None)
#     n=0
#     while n<5:
#         n=n+1
#         print('[PRODUCE] producing %s...'% n)
#         r=c.send(n)
#         print('[PRODUCER] Consumer return:%s'%r)
#     c.close()

# c=consumer()
# produce(c)

# #asyncio
# @asyncio.coroutine
# def hello():
#     print('Hello world!')
#     #异步调用 asyncio.sleep(1)
#     r=yield from asyncio.sleep(3)
#     print('Hello again!')

# #获取EventLoop:
# loop=asyncio.get_event_loop()
# #执行coroutine
# loop.run_until_complete(hello())
# loop.close()



# @asyncio.coroutine
# def hello():
#     print('Hello world!(%s)'%threading.currentThread())
#     yield from asyncio.sleep(2)
#     print('Hello,again!(%s)'%threading.currentThread())

# loop=asyncio.get_event_loop()
# tasks=[hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# @asyncio.coroutine
# def wegt(host):
#     print('wget %s...'%host)
#     connect=asyncio.open_connection(host,80)
#     reader,writer=yield from connect
#     header= 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line=yield from reader.readline()
#         if line==b'\r\n':
#             break
#         print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
#     #Ignore the body,close the socket
#     writer.close()

# loop=asyncio.get_event_loop()
# tasks=[wegt(host) for host in ['www.sina.com.cn','www.baidu.com','www.qq.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# #async/await
# async def hello():
#     print('Hello world!')
#     r=await asyncio.sleep(2)
#     print('Hello again!')

# #获取EventLoop:
# loop=asyncio.get_event_loop()
# #执行coroutine
# loop.run_until_complete(hello())
# loop.close()


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9999)
    print('Server started at http://127.0.0.1:9999...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
