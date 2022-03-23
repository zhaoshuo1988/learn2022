#模块导入
from socket import *

#声明服务器IP，端口
ADDR = ('0.0.0.0',8888)

#创建udp套接字  SOCK_DGRAM 表示选择的是UDP套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

#调用bind 绑定地址端口
udp_socket.bind(ADDR)

#循环接受消息
while True:
    #接收消息 1024表示异常能接受的最大字节数
    msg,addr=udp_socket.recvfrom(1024)
    #打印消息跟地址 decode()解码
    print('Recv:',addr,msg.decode())
    #回应消息
    udp_socket.sendto("收到".encode(),addr)
    #约定断开通信的 暗号
    if msg ==b'bye':
        break

#关闭套接字，释放资源
udp_socket.close()
