class big(object):
    def __init__(self):
        pass
        print("父类中的初始化")

    def a(self):
        print("父类中的方法")


class small(big):
    def __init__(self):
        super(big).__init__()
        # 传入参数后
        pass

    def a(self):
        # print("子类中的方法")
        print(super().a())


子类 = small()
子类.a()
