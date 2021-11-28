# from multiprocessing import Pool
# import os,random ,time
# import multiprocessing

# def work(num):
#      for i in range (5):
#          print('===pid=%d==num=%d='%(os.getpid(),num))
#          time.sleep(1)
# # 3表示进程池中最多有三个进程一起执行
# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#     pool=Pool(5)
#     for i in range(5):
#         print("---%d---"%i)
#         # 向进程中添加任务
#         # 注意：如果添加的任务数量超过了进程池中进程的个数的话，那么就不会接着往进程池中添加，如果还没有执行的话，他会等待前面的进程结束，然后在往
#         # 进程池中添加新进程
#         pool.apply_async(work,(i,))
#         pool.apply(work,(i,))
#     pool.close()#关闭进程池 
#     pool.join()#主进程等待，只有所有的子进程结束之后，然后父进程才能结束
#     #进程之间执行的顺序不能够保证


import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

def  func(value):
    time.sleep(1)
    print(value)


pool = ThreadPoolExecutor(max_workers=5)


for i in range(10):
    fut =pool.submit(func,i)
    print(fut)
