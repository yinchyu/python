from socket import *
import time
import socket

# 组播组IP和端口
mcast_group_ip = '10.0.11.255'
mcast_group_port = 5000
def sender():
    # 建立发送socket，和正常UDP数据包没区别,但要设置socket.IPPROTO_UDP
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 每十秒发送一遍消息
    # 猜测只可能是网卡自己在识别到目的ip是组播地址后，自动将目的mac地址设为多播mac地址
    print(mcast_group_ip, mcast_group_port)
    while True:
        message = "this message send via mcast !"
        # 发送写法和正常UDP数据包的还是完全没区别
        send_sock.sendto(message.encode(), (mcast_group_ip, mcast_group_port))
        print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: message send finish')
        time.sleep(0.5)

if __name__ == "__main__":
    sender()

