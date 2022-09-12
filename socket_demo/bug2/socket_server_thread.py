# -*- coding:utf-8 -*-

import socket
import threading


def link_handler(link, client):
    print('server start to receiving msg from [%s:%s]....' % (client[0], client[1]))
    while True:
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print('communication end with [%s:%s]...' % (client[0], client[1]))
            break
        print('client from [%s:%s] send a msg：%s' % (client[0], client[1], client_data))
        link.sendall('server had received your msg'.encode())
    link.close()


ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
# bug：需要bind ip	
sk.bind(ip_port)
sk.listen(5)

print('start socket server，waiting client...')

while True:
    conn, address = sk.accept()
    print('create a new thread to receive msg from [%s:%s]' % (address[0], address[1]))
    # 每当有新的连接过来，自动创建一个新的线程，
    # 并将连接对象和访问者的ip信息作为参数传递给线程的执行函数
    t = threading.Thread(target=link_handler, args=(conn, address))
    # bug处：线程必须调用start启动
    # t.start()
