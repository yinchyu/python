import socket
import threading
from time import ctime
def recv(sock,buffer_size):
    try:
        data=sock.recv(buffer_size)
    except OSError :
        return # 发现连接关闭， 然后关闭连接
    if data.decode() is "[CHAT]BEGIN":
        print(data.decode())
    elif data.decode() is "[CHAT]END":
        sock.size()
    else:
        print('[%s]'%ctime(),':',data.decode())
if __name__ == "__main__":
    tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp.connect(('192.168.2.40',8090))
    # tcp.connect(('192.168.43.241',8080))
    t1=threading.Thread(target=recv,args=(tcp,1024))
    t1.start()
    t=1
    while True:
        data=input('请输入数据：')
        if not data:
            break
        tcp.send(data.encode())
    tcp.close()
