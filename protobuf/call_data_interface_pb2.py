# -*- coding: utf-8 -*-

from data_interface_pb2 import wav,wavlist
# 从生成的proto中导入对应的类， 类方法在protobuf中进行了描述
alist=wavlist()
# wav 中的是对应的wav 中的具体的字段， 但是wav 对应的是 label wav 对象
for i in range(10):
    # 使用对象的add 函数表示新添加一个对象，然后再对对象进行赋值操作，然后进行序列化操作
    # 三步走战略，对个repeated 限定的字段也可以通过字段进行区分，
    a=alist.multiwav.add()
    # 对一个a 的protobuf 的结构体进行赋值
    a.msgtime=1
    a.number=1
    a.wavlen=3.4
    a.info="hello"
    c=alist.multifpi.add()
    c.name="12"


seriallist=alist.SerializeToString()
# 转换过后就是二进制的字节数据
print(type(seriallist),seriallist)
a=wav()
a.msgtime = 1
a.number = 1
a.wavlen = 3.4
a.info = "hello"
# alist.wavlist.add(a)
# for i in range(10):
#     alist.label.add(a)
c=wav()

# 从别的对象中拷贝一份数据过来到新的对象中，
c.CopyFrom(a)
print(c.ByteSize(),c)
b=wavlist()
b.ParseFromString(seriallist)
# 可以使用ByteSize 获取对应的序列化后的长度
# print(b.ByteSize())
# 调用b.Clear() 就可以清空一个protobuf 的list 的长度
# b.Clear()
# findinitializationErrors()  返回的是一个对应的列表
#'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', '_SetListener',
print("*********",b.FindInitializationErrors())
print(b.ListFields())
print("^"*40)
print("--------",len(b.multiwav),b.ByteSize())
for i in b.multiwav:
    print(i.info)

# 返回的是序列化的长度， 不知道部分序列化和全部序列化的区别



