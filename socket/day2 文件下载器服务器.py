import socket
import threading


if __name__ == '__main__':
    tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp.bind(("",8090))
    tcp.listen(2)
    new_socket,adress=tcp.accept()
    with open('tcptext.txt','rb') as f:
        content=f.read()
    new_socket.send(content)
    new_socket.close()
    tcp.close()





