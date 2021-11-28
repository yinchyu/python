# 返回结构体
import ctypes

path = r'./share_data.dll'
dll = ctypes.WinDLL(path)

#定义结构体
class StructPointer(ctypes.Structure):  #Structure在ctypes中是基于类的结构体
    _fields_ = [("name", ctypes.c_char * 20), #定义一维数组
                ("age", ctypes.c_int),
                ("arr", ctypes.c_int * 3),   #定义一维数组
                ("arrTwo", (ctypes.c_int * 3) * 2)] #定义二维数组

#设置导出函数返回类型
dll.test.restype = ctypes.POINTER(StructPointer)  # POINTER(StructPointer)表示一个结构体指针
#调用导出函数
p = dll.test()

print(p.contents.name.decode())  #p.contents返回要指向点的对象   #返回的字符串是utf-8编码的数据，需要解码
print(p.contents.age)
print(p.contents.arr[0]) #返回一维数组第一个元素
print(p.contents.arr[:]) #返回一维数组所有元素
print(p.contents.arrTwo[0][:]) #返回二维数组第一行所有元素
print(p.contents.arrTwo[1][:]) #返回二维数组第二行所有元素
