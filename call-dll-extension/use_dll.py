import ctypes


fibo = ctypes.CDLL('./fibo.dll')
# 在c语言中需要通过一行代码对函数设置为导出类型
# extren "C" __declspec(dllexport)
# extern "C" __declspec(dllexport)

result = fibo.fibo(10)
#fibo.getdata.argtypes =[ctypes.c_char_p,或者是其他的类型的变量]
fibo.getdata.restype = ctypes.c_char_p# 指定函数的返回类型
# 如果ctypes 默认返回的类型是int 类型， 如果要返回其他的类型需要通过restype 来进行指定
string = fibo.getdata(b'hello')
print(result)
print(string.decode())

