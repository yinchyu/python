#encoding=utf8
import time
import socket
def receiver():
    # 建立接收socket，和正常UDP数据包没区别
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 只用在接受方设置端口重用，就可以绑定一个地址想
    # 默认查找的是第一个的配置
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1000)
    # 获取本地IP地址
    sock.bind(('192.168.1.255',4001))
    while True:
        try:
            message, addr = sock.recvfrom(65535)
            print(time.asctime(), "Receive data from",addr)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    receiver()
