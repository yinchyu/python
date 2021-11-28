
import time
import os
def process():
    nun=0
    while True:
          n=yield nun
          a="接受到的数据是 NO.{}".format(n)
          os.system('echo {} >> /dev/pts/1'.format(a))
          nun+=1

def main():
    g= process()
    h=g.send(None)
    print("第一次接受到数据",h)
    # 第一次传递为空相当于next 调用， 初始化不能传递数据，
    num=1
    while True:
        print("发送的数据是 NO.",num)
        res=g.send(num)
        print("第二次接受到数据",res)
        num+=1
        
        ##print("接受到的数据是{}".format(res))
        time.sleep(0.5)
if __name__ == '__main__':
    main()
