# import  sys
moudle_name = __import__("os")
path_name = __import__("os.path",fromlist=True)
# 内部的模块必须通过fromlist = true , 来进行递归的导入
join_name=getattr(path_name,"join")
print(join_name("good","study"))
print(getattr(path_name,"join"))

print(hasattr(path_name,"dirname"))
#表示内部有dirname 这个函数
print(setattr(path_name,"good",__file__))
print(hasattr(path_name,"good"))
print(getattr(path_name,"good"))
# 可以直接设置一个包的内部的属性
print(delattr(path_name,"good"))
# 删除和设置属性都是直接对应返回值none
print(getattr(moudle_name,"listdir"))
dir_list=getattr(moudle_name,"listdir","notfound")
if dir_list=="notfound":
    print("未找到函数")
    # print(dir_list)
else:
    print(dir_list(r"C:\Users\11928\Desktop\pythontest"))
    # 获取属性然后通过返回值，进行调用
    # print(dir_list)


# callable()判断一个函数是否可以被调用
# print(globals()[__name__])
# globals() 中存放的是一个字典的形式， 包括了一些属性