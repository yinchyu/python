# import socket
# import time
# udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# dgram 表示报文数据，是udp协议
# udp.bind(('192.168.43.241',8090))#绑定端口地址然后进行监听
# # data=udp.listen()
# while True:
#       data=udp.recvfrom(1024)# 设置udp的接受数据的bufersize
#       print(data[0].decode('utf-8'))
#       #0:b'\xca\xc0\xbd\xe7\xc4\xe3\xba\xc3'
#       #1:('192.168.43.241', 8080) data同时将发送方的地址显示出来
import socket

udp= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(('',9000))
while True:
      print('等待接收数据----')
      data=udp.recvfrom(1024)
      print('接收的数据为： ',data[0].decode('utf-8'))