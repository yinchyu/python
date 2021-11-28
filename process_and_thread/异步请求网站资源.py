import asyncio
import requests
import time

num=0
a=list()
def func(fn):
	async def inner(*args):
	   start= time.time()
	   await fn(*args)
	   time_spend = time.time()- start
	   if args==tuple():
	   	  pass
	   	  # print("总共用的时间是{}".format(time.time()-a[0]))
	   else:
	      print("{}用的时间是{}".format(args[0],time_spend))
	   
	return inner

@func
async def curl(hostname):
	global num
	print("请求网站{}的资源...".format(hostname))
	await asyncio.sleep(0.0000000001)
	#  交出线程的控制权
	result =  requests.get(hostname)
	 #  协程中如果不主动的进行控制， 协程执行的函数也是不会交出控制权， 必须通手动的控制 await 来实现

	# await result
# TypeError: object Response can't be used in 'await' expression
	
	# 等待一个任务对象，在一个协程中必须有一个可以await 的对象 就是说必须有一个耗时的IO操作，在前面加上await
	if result.status_code==200:

		with open ("{}.html".format(num),'w',encoding='utf-8')as f:
			f.write(result.text)
			num+=1
	else:
		print("请求失败...")
@func
async def main():
	beg = time.time()
	tasks=[asyncio.create_task(curl(i)) for i in [' http://www.sohu.com', ' http://www.163.com', ' http://www.163.com', ' http://www.163.com', ' http://www.163.com', \
	' http://www.163.com', ' http://www.163.com', ' http://www.163.com', ' http://www.163.com', ' http://www.163.com']]
	await asyncio.gather(*tasks)
	stop =time.time()-beg
	print("总共用的时间是{}".format(stop))

	#  表示将所有的tasks 加入到循环事件中

# await asyncio.wait(tasks)，在函数外部不能使用， 只能使用asyncio.run()\


if __name__ == "__main__":
	

	asyncio.run(main())
	print("所有的任务执行结束...")
	# loop = asyncio.get_event_loop()
	# tasks = [curl(host) for host in [' http://www.sohu.com', ' http://www.163.com']]
	# loop.run_until_complete(asyncio.wait(tasks))
	# loop.close()







