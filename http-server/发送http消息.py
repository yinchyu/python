import socket
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing.pool import ThreadPool
tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.bind(('',8090))
tcp.listen(5)
#使用threadpool
pool=ThreadPool(3)
# 进程池中间创建3个线程， 但是调用的堆栈产生了6个线程， 如果使用单线程可能发生线程先结束导致数据发送不过去的情况

#使用executor


## 发送数据
def process(sock,ret):
    data='HTTP/1.1 200 OK\r\n\r\n'#中间需要一个空行
    sock.send(data.encode())
    try:
       f= open(ret,'rb')
    except:
        sock.send(b'')
        pass
    else:
        content=f.read()
        sock.send(content)
        f.close()
        sock.close()

if __name__ == '__main__':
    
    while True:
        new_socket,address=tcp.accept()# 每次发送请求就有accept，可能是建立的多次的tcp连接，不是一次
        data=new_socket.recv(2048).decode('utf-8')
        if data=='':
            data='HTTP/1.1 200 OK\r\n\r\n'#中间需要一个空行
            new_socket.send(data.encode())
            continue
        elif not data:
            break
        print('>'*30)
        print(data)
        datalines=data.splitlines()
        url=re.search(r'/(.*) HTTP/1.1$',datalines[0])
        if url!=None and url.group(1)!='':
            ret=url.group(1)
        else:
            ret='index.html'
        print(ret)
        #使用pool
        pool.apply_async(process,args=(new_socket,ret))
        
        
        # 使用exectuer，未执行成功，具体功能不清楚
        # with ThreadPoolExecutor(max_workers=3) as t:
        #     t.submit(process,(new_socket,ret))
    tcp.close()


