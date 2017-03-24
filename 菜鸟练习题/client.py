import socket
import sys

#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名字
host = socket.gethostname()

#设置端口
port = 9999

#连接服务
s.connect((host,port))

msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))