def gen():
    i = 0
    while True:
        i = i + 1
        rec = yield i
        print("收到的数据是", rec)
        print("-------------")


if __name__ == "__main__":
    c = gen()
    c.send(None)
    for i in range(99):
        r =c.send(str(i+1))
        print("返回的的数据", r)

# 也是设置的端点， 然后从函数返回后执行

