#模块导入
from socket import *
#如果用import socket,则创建时应用socket.socket()

#确定服务器地址 
ADDR = ('127.0.0.1',8888)

#创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
#地址端口可绑定，可不绑定，客户端默认由操作系统自动分配

#循环发送消息
while True:
    #接受消息
    msg = input('>>:')
    #发送给服务器
    udp_socket.sendto(msg.encode(),ADDR)
    #接受服务器的消息
    data,addr = udp_socket.recvfrom(1024)
    print('来自服务器的消息：',data.decode())
    #终止客户端循环
    

#关闭套接字，释放资源
udp_socket.close()
