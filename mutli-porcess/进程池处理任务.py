import time,random,os
# from multiprocessing import Pool
import multiprocessing
from multiprocessing import freeze_support

def worker(i):
    time_start=time.time()
    print('进程：{}开始的时间是：{}'.format(i,time_start))
    print('进程: {}的pid是:{}'.format(i,os.getpid()))
    random_time=random.random()
    time.sleep(random_time*2)
    time_stop=time.time()
    print('进程：{} 结束的时间是：{},   运行的时间是：{}'.format(i,time_stop,(time_stop-time_start)))
def main():
    pass
    


if __name__ == '__main__':
    freeze_support()
    po=multiprocessing.Pool(3)
    print('------- 开始执行进程池----------')
    for i in range(20):
        po.apply_async(worker,(i,))
    po.close()# 关闭进程池， 不让进程池接受其他的任务
    po.join()# 等待子进程的执行完成， 然后结束进程池，结束主进程，

    print('--------- 进程池的执行结束---------')
    



