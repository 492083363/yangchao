#!/bin/python
import socket
import sys
# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设定最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsockt, addr = serversocket.accept()
    print("{}连接地址".format(addr))
    msg = '欢迎访问！' + "\r\n"
    clientsockt.send(msg.encode('utf-8'))
    clientsocket.close()
