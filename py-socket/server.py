# server

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET)

ip = ()

server.bind(ip)

server.listen()

conn, addr = server.accept()
print("")


