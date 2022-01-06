import time
import multiprocessing

num=0
n=multiprocessing.Queue(10)#  设置一种队列模式，然后进行操作，可以看做是按照队列进行通信
def test1(n):
    global num
    # for i in range(20):
    #     if n.full():
    #        print('放入的数据满了')
    #     else: 
    #         n.put(i)
    # print('放入数据完成') 
    for i in range(20):
        if not n.full():
           n.put_nowait(i)
        else:
            print('数据放满了')

def test2(n):
    global num
    if not n.empty():
        for i in range(n.qsize()):
            print(n.get_nowait())
        
        k=n.get()
        print(k)
    print('读取数据完成')

def main():
    p1=multiprocessing.Process(target=test1,args=(n,))
    p2=multiprocessing.Process(target=test2,args=(n,))
    p1.start()
    p2.start()

    pass


if __name__=='__main__':
    main()