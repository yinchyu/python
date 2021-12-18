def consumer():
    r = ''
    while True:
        n = yield r
        # 进行分段执行
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 给一个yield 传递数据
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == "__main__":
    c = consumer()
    # 返回的结果是一个生成器
    produce(c)
