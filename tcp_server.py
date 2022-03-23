#导入模块

from socket import *


#创建套接字,默认TCP socket_stream流式套接字

tcp_socket=socket(AF_INET,SOCK_STREAM)

#绑定地址
tcp_socket.bind(('0.0.0.0',8888))

#设置监听  Listen最大能设置1024个。linux自动配置
#具备监听属性，被客户端连接的属性
tcp_socket.listen(5)


#等待客户端连接
print('等待客户端连接中……')
while True:
    #accept()阻塞函数，等待处理客户端连接请求，没有连接则阻塞
    #connfd处理该链接的专门套接字
    #addr 客户端地址
    connfd,addr = tcp_socket.accept()
    print('连接的客户端是：',addr)

    #处理客户端的信息
    i=0
    while i==0:
        data = connfd.recv(1024)
        if data.decode()!='bye':
            print('消息:',data.decode())
            connfd.send('收到!'.encode())
        else:
            print('消息:',data.decode())
            i = 1
    else:
        print('{}客户端断开连接'.format(addr))
        connfd.send('bye'.encode())
        connfd.close()
    
        
else:
    connfd.send('bye'.encode())
    
    
#关闭连接
    
tcp_socket.close()

