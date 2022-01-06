import time
def test1():
    while True:
        print('-----1-----')
        time.sleep(0.2)
        yield
def test2():
    while True:
        print('-------2-----')
        time.sleep(0.2)
        yield
def main():
    t1=test1()
    t2=test2()
    num=0
    while True:
        next(t1)
        next(t2)
        num+=1
        if num>20:
            break

if __name__ == '__main__':
    main()


