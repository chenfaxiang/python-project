#!/usr/bin/env python
# -*- coding: utf-8 -*-

' socket server端 '
__author__ = 'ChenFaxiang'

import socket

# 创建一个socket实例
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip
sock.bind('192.168.0.53', 8080)

# 进行监听
sock.listen(5)
    # 参数是监听的队列长度

print('server is start>>')

# 进行接收
con,(add, port) = sock.accept()
    # accept 返回的内容
    # 第一部分 一个用来j接收和发送信息的socket实例
    # 第二部分 客户端ip和端口号

while True:
    sendData = raw_input('>>>')
    con.send(sendData)
    recvData = con.recv(512)
    print(recvData)

print('%s:%s is connnetd'%(add, port))

# con.send('hello, i am your server')

print(con.recv(512))

sock.close()
