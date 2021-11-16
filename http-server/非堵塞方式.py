import socket
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(('',8090))
tcp_server.listen(5)

#设置tcpsocket 不堵塞
tcp_server.setblocking(False)
socket_list=list()
while True:#循环为多个socket服务
    try:
        new_socket,addr= tcp_server.accept()
    except:
        print('------当前没有客户端连接------')
    else:
        new_socket.setblocking(False)
        socket_list.append(new_socket)

    
    for sock in socket_list:
        try:
            data= sock.recv(1024)
            print(data.decode())
        except:
            print('----- 客户端没有发送来数据-----')


