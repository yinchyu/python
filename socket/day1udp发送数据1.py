import socket
import time
import struct
import datetime
 
# with open("fly.txt","rb") as f:
# 	a=f.read()
data = b'\x1b' + 47 * b'\0'

udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# dgram 表示报文数据，是udp协议

print('---发送数据---')
udp.sendto(data,('192.168.2.40',123))
data,address=udp.recvfrom(1024)
print(data)
print(address)
date_res = struct.unpack("!12I",data)[10]-2208988800
timestr=time.strftime('%Y %m %d %H %M %S',time.localtime(date_res))
dt=datetime.datetime.strptime(timestr,'%Y %m %d %H %M %S')
print(dt)
udp.close()




