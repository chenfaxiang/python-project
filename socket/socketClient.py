#!/usr/bin/env python
# -*- coding: utf-8 -*-

' socket client端 '
__author__ = 'ChenFaxiang'

import socket

# 创建一个socket实例
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 进行连接
sock.connect(('192.168.0.53', 8080))
    # 链接时写上服务端指定的ip和端口号

# while True:
#    recvData = sock.recv(512)


sock.send('hello, i am your client')

sock.close()
