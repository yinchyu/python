import socket
import select


tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(('',8090))
tcp_server.listen(5)



#设置tcpsocket 不堵塞
tcp_server.setblocking(False)
socket_list=list()

# 设置epoll 并注册事件
epl=select.epoll()

#将监听套接字的fd注册到对应的epoll中
epl.register(tcp_server.fileno(),select.EPOLLIN)

# 设置字典方便将fd中回复文件的监听套接字
#key:fileno   value:socket
fd_event_no=dict()


while True:
    fd_event_list=epl.poll()# 检测到有事件通知会poll解堵塞
    for fd,event in fd_event_list:
        if fd==tcp_server.fileno():
            new_socket,new_addr=tcp_server.accept()#对连接产生的新的套接字进行注册
            epl.register(new_socket.fileno(),select.EPOLLIN)
            fd_event_no[new_socket.fileno()]=new_socket
        elif event == select.EPOLLIN:
            recv_data=fd_event_no[new_socket.fileno()].recv(1024).decode()
            if recv_data:
                print(recv_data)
            else:
                fd_event_no[new_socket.fileno()].close()
                socket_list.remove(fd_event_no[new_socket.fileno()])
                
            
            





# while True:#循环为多个socket服务
#     try:
#         new_socket,addr= tcp_server.accept()
#     except:
#         print('------当前没有客户端连接------')
#     else:
#         new_socket.setblocking(False)
#         socket_list.append(new_socket)

    
#     for sock in socket_list:
#         try:
#             data= sock.recv(1024)
#             print(data.decode())
#         except:
#             print('----- 客户端没有发送来数据-----')


