# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 9999)

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.SOCK_STREAM is tcp
#sk = socket.socket()
sk.bind(ip_port)
# tcp has to use a listener
sk.listen(5)
print('start socket server，waiting client...')
conn, address = sk.accept()
print(address, ' connected...')
while True:
    client_data = conn.recv(1024).decode()
    if client_data == "exit":
        exit('communication end.')
    print('the client from %s sends msg ：%s' % (address, client_data))

    conn.sendall('server has receive your msg.'.encode())
conn.close()
