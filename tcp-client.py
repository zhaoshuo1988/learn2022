#导入模块
import socket

#创建套接字
tcp_socket = socket.socket()

#连接服务端 127.0.0.1回环测试
 # 0.0.0.0 无效地址
tcp_socket.connect(('127.0.0.1',8888))

while True:
    #发送消息
    msg = input('>>:')
    tcp_socket.send(msg.encode())

    #接收服务端的消息
    data = tcp_socket.recv(1024)
   

    print('服务端:',data.decode())
    if data.decode() =='bye':

        break

#关闭连接
tcp_socket.close()

    

