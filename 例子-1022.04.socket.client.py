#coding=utf-8
import socket
ip_port=('127.0.0.1',9999)
sk=socket.socket()
#链接address套接字
sk.connect(ip_port)
sk.sendall(('server server im client!!').encode())
ser_reply=sk.recv(1024)
print(ser_reply)
sk.close()
