import socket
import threading
from multiprocess.pool import ThreadPool
import queue
# 设置套接字
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.bind(('',8090))
tcp.listen(10)# 设置连接的用户数
#创建一个new——socket队列
q=queue.Queue(10)

# 创建一个线程池来分发tcp连接
# p=ThreadPool(1)

#处理客户端的链接
def link_tcp(tcp):
    while True:
        new_socket=tcp.accept()
        q.put(new_socket)
        # 设置发送数据和接受数据

def process_data(new_socket):
    while True:
        data=new_socket[0].recv(1024)
        if not data:
            new_socket[0].close()
        else:
            print('接受来自{}的数据: {}'.format(new_socket[1],data.decode()))
            # new_socket[0].send('copy send data'.encode())
            new_socket[0].send(('your ip： {}  port：{} '.format(new_socket[1][0],new_socket[1][1])).encode())
            with open('tcptext.txt','a+') as f:# 使用线程不能保证顺序的有序执行， 所以写入的顺序也不是有序的执行
                f.writelines(data.decode())
            


if __name__ =="__main__":

    #设置一个线程等待tcp连接
    t1=threading.Thread(target=link_tcp,name='wait_tcp',args=(tcp,))
    t1.start()
    joinlist=list()
    while True:
        new_socket=q.get()
        # process_data(new_socket)
        t=threading.Thread(target=process_data,name='process_data',args=(new_socket,))
        t.start()
        joinlist.append(t)
    map(lambda x: x.join(),joinlist)
    t1.join()
    tcp.close()
   









