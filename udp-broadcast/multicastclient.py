import struct
import time
import socket

# 组播组IP和端口
mcast_group_ip = '225.25.25.25'
mcast_group_port = 5000

def receiver():
    # 建立接收socket，和正常UDP数据包没区别
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 只用在接受方设置端口重用，就可以绑定一个地址想
    # 默认查找的是第一个的配置
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1024)
    # 获取本地IP地址
    local_ip = socket.gethostbyname(socket.gethostname())
    print(socket.gethostname())
    # 可以直接通过 socket.getostbyname(socket.gethostname()),获取到对应的
    local_ip="0.0.0.0"
    print(local_ip)

    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    # 绑定的是本地的组播的端口号， 组播是往这个端口进行发送
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组 s 是char[]  不确定的字节个数,l是long 4个字节
    # mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    #print(mreq)
    # print(socket.inet_aton(mcast_group_ip))
    # 直接将一个int0 转换成为4个自己的数据
    #如果是1个s 表示直接截取对应字符串的一位，如果是b 的话表示将integer 转换成字节
    # print(struct.pack("4s",socket.inet_aton(mcast_group_ip)))
    # print(struct.pack("l",0))
    # sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
    # sock.settimeout(3)
    # 允许端口复用，看到很多教程都有没想清楚意义是什么，我这里直接注释掉
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO;/_REUSEADDR, 1)
    # 设置非阻塞，看到很多教程都有也没想清楚有什么用，我这里直接注释掉
    # sock.setblocking(0)
    while True:
        try:
            message, addr = sock.recvfrom(65535)
            print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: Receive data from {addr}: {message.decode()}')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    receiver()
