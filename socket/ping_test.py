from threading import Thread
import socket
import time
num =0

import os
def ping(i,j):
    command = "ping -n 1 192.168.{}.{}".format(i,j)
    print("192.168.{}.{}".format(i,j) + "的请求已经发出...")
    res = os.system(command)
    if not res:
        with open("connecting_ok.txt", "a+")as f:
            f.write(command + "\n")
        print(command, "is OK...")
    else:
        print(command, "is not OK...")
        with open("connecting_not_ok.txt", "a+")as f:
            f.write(command + "\n")
        pass
def keepthread():
   global num
   num+=1
   print("这个是开启的{}线程".format(num))
   sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   time.sleep(15)



if __name__ =="__main__":
    for i in range(1,2):
        for j in range(1,255):
             Thread(target=ping,name="线程{:>3d}".format(num),args=(i,j)).start()


     