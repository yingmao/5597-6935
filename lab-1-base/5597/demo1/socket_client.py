# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 9999)

s = socket.socket()
s.connect(ip_port)

while True:
    inp = input('input msg： ').strip()
    if not inp:
        continue
    s.sendall(inp.encode())

    if inp == "exit":
        print("communication end！")
        break

    server_reply = s.recv(1024).decode()
    print(server_reply)
s.close()
