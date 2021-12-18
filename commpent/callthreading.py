import threading
import time
import os
 
# 原本需要用来启动的无线循环的函数
def print_thread():
 pid = os.getpid()
 counts = 0
 while True:
  print(f'threading pid: {pid} ran: {counts:04d} s')
  counts += 1
  time.sleep(1)
 
# 把函数放到改写到类的run方法中，便可以通过调用类方法，实现线程的终止
class StoppableThread(threading.Thread):
 
 def __init__(self, daemon=None):
  super(StoppableThread, self).__init__(daemon=daemon)
  self.__is_running = True
  self.daemon = daemon
 
 def terminate(self):
  self.__is_running = False
 
 def run(self):
  pid = os.getpid()
  counts = 0
  # 可以在子线程中的while  True 中设置参数进行解决
  while self.__is_running:
   print(f'threading running: {pid} ran: {counts:04d} s')
   counts += 1
   time.sleep(1)
 
def call_thread():
 thread = StoppableThread()
 thread.daemon = True
 thread.start()
 
 pid = os.getpid()
 counts = 0
 for i in range(5):
  print(f'0 call threading pid: {pid} ran: {counts:04d} s')
  counts += 2
  time.sleep(2)
 # 主动把线程退出
 thread.terminate()
 
if __name__ == '__main__':
 call_thread()
 print(f'==========call_thread finish===========')
 counts = 0
 for i in range(5):
  counts += 1
  time.sleep(1)
  print(f'main thread:{counts:04d} s')
