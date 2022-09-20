import socket
BUFSIZE = 1024

ip_port = ('127.0.0.1', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
server.bind(ip_port)

print('start socket server，waiting client...')
while True:
    data,client_addr = server.recvfrom(BUFSIZE)
    print('server received data : ', data)

    server.sendto(data.upper(),client_addr)

server.close()
