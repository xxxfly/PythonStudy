#-*-coding:utf-8-*-

import select
import socket
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7789))
server.listen(5)

inputs = [server, sys.stdin]

running = True

while True:

    # 调用 select 函数，阻塞等待
    readable, writeable, exceptional = select.select(inputs, [], [])

    # 数据抵达，循环
    for sock in readable:

        # 监听到有新的连接
        if sock == server:
            conn, addr = server.accept()
            print('新客户端链接：%s'%str(addr))
            # select 监听的socket
            inputs.append(conn)

        # 监听到键盘有输入
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break

        # 有数据到达
        else:
            # 读取客户端连接发送的数据
            data = sock.recv(1024)
            print('接收数据-->%s'%data)
            if data:
                sock.send(data)
            else:
                # 移除select监听的socket
                inputs.remove(sock)
                sock.close()

    # 如果检测到用户输入敲击键盘，那么就退出
    if not running:
        break

server.close()