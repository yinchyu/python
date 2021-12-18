import threading
import os
import time
class mythread(threading.Thread):
    def __init__(self):
        super(mythread, self).__init__()
        self.__runthreading=True
    # 使用线程的时候重写run 函数，继承的是threading.Thread
    def run(self):
        while self.__runthreading:
            print(os.getpid())
            time.sleep(0.5)
    def teminate(self):
        self.__runthreading=False

a=mythread()
a.start()

print(os.getpid())
time.sleep(5)
a.teminate()

