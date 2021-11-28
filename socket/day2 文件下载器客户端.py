import socket

if __name__ == '__main__':
    tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp.connect(('192.168.43.241',8090))
    data=tcp.recv(1024*1024)# 设置一次传输接受的数据的大小， 一般文件过大需要分次接受
    if not data:
        tcp.close()
    else:
        with open('new_tcp.txt','wb') as f:# 写入文件
            f.write(data)
    