import threading
import time
import ctypes

# func =ctypes.windll.LoadLibrary(r'D:\c++_programs\untitled1\cmake-build-debug\libuntitled1.dll')
func =ctypes.CDLL(r'D:\c++_programs\untitled1\cmake-build-debug\libuntitled1.dll')
print(func)
# def count():
# 	num=0
# 	while True:
# 		print("NO is ",num)
# 		num=num+1

if __name__ == '__main__':
	a=threading.Thread(target=func.he)
	a.setDaemon(True)
	a.start()
	time.sleep(10)
	
