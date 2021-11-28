import socket
import threading
from time import ctime
def recv(sock1,sock2,buffer_size):
    while True:
        try:
            data=sock1.recv(buffer_size)
        except OSError :
            break # 发现连接关闭， 然后关闭连接
        if not data:
            sock1.close()
        else:
            try:
                sock2.send(data)
            except OSError:
                sock1.close()
                break

if __name__ == "__main__":
    tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # tcp.bind(('192.168.43.241',8090))
    tcp.bind(('',8090))
    #让默认的套接字由主动变成被动模式
    tcp.listen(3)# 最多设置三个连接，监听套接字， 只是负责监听， 然后accept () 产生新的套接字负责产生服务
    server=list()# 直接改成服务器产生的套接字
    adds=list()
    trans=list()
    while len(server)!=2:
        # 等待被人的connect连接
        content,addrs=tcp.accept()# 接受用户的连接后产生的服务套接字， 然后，user[1] 就是为用户1 服务，recv 就是接受用户1发送的数据
        server.append(content)# 有新的套接字建立连接，就是解堵塞，产生一个newclient
    t1=threading.Thread(target=recv,args=(server[0],server[1],1024))
    t1.start()
    while True:
        try:
            data=server[1].recv(1024)# 表示用户1是否发送了数据
        except OSError:
            break
        if not data:
            server[1].close()
        else:
            try:
                server[0].send(data)# user[0] 就是服务端产生的服务套接字发送数据， 给客户端[0]  发送的数据是客户端[0]发送给服务端的
            except OSError:
                server[1].close()
                break
    tcp.close()# 关闭监听套接字之后就不能进行客户端的请求 即tcp.accept()会失败

