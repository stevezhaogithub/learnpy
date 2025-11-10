# client

import socket

# 创建客户端对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建目标 ip 和 port
target = ("ip", port)

# 客户端连接服务器
client.connect(target)

