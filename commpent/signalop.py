import signal
import sys
import threading
import time
def ctrlz():
    def myhandler(signalnum, frame):
        print("i receive number ",signalnum)

    signal.signal(signal.SIGTSTP,myhandler)

    signal.pause()
    print(" end of signal demo")


def timer():
    def myhandler2(signalnum, frame):
        print("NOW , it's the time ")
        exit()

    signal.signal(signal.SIGALRM,myhandler2)
    signal.alarm(3)
    # 设置时钟给 while True 发送信号
    # os.kill(pid, sid),或者时间到了之后直接通过os.kill 进行操作
    while True:
        print('nor yet')

def process():
    while True:
        print('nor yet')
    
    
if __name__ == '__main__':
    #timer()
    a=threading.Thread(target=process)
    a.setDaemon(True)
    a.start()
    # 设置守护线程的诀窍就是start() 必须要在setDaemon 后边启动
    #a.join() 表示等到a结束才会执行主线程下边的语句， 一般放在主线程的最后一句执行， 就是等待子线程执行完成才推出子线程
    time.sleep(2)

