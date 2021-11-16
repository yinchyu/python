import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()
tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.bind(('',8090))
tcp.listen(5)

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
        #使用gevnet spwan  yield 也是协程
        gevent.spawn(process,new_socket,ret)#参数直接写到后边就可以不用卸载tuple中



    tcp.close()


