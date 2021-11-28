import socket
import time
import threading

def send_rec_data(sock):
    while True:
        sock.send('ycy\n'.encode())
        data=sock.recv(1024)
        print('--------------')
        print(data.decode())
        # time.sleep(1)
        

if __name__ =='__main__':
    joinlist=list()
    for i in range(5):
        tcp_name=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_name.connect(('39.107.248.167',8090))
        t1=threading.Thread(target=send_rec_data,name='sock_'+str(i),args=(tcp_name,))
        t1.start()
        joinlist.append(t1)
    map(lambda x: x.join(),joinlist)


