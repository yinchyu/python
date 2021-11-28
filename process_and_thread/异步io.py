# import time
# import asyncio
#
#
# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
# async def main(urls):
#     for url in urls:
#         # await是同步调用, crawl_page(url)在当前的调用结束之前, 是不会触发下一次调用的
#         await crawl_page(url)
# #          必须使用await 否则会产生错误 runtimeWarning: coroutine 'crawl_page' was never awaited
#
# start = time.perf_counter()
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# end = time.perf_counter()
# print(end - start)

#
# import time
# import asyncio
#
#
# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     # time.sleep(sleep_time)
#     #  在异步中的时间等待和同步中的时间等待不知道有什么不同
#     print('OK {}'.format(url))
#
#
# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     # 创建任务之后就直接执行了
#     # *tasks解包列表, 将列表变成了函数的参数
#     await asyncio.gather(*tasks)
#     # 等待所有的任务执行完毕
#     # 不加这个时间的等待也是可以的，但是等待的时间必须是在time.sleep()中，或者使用
#     # for task in tasks:
#     #     await task
#
# start = time.perf_counter()
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# end = time.perf_counter()
# print(end - start)

#!usr/bin/python
# -*- coding:utf8 -*-
"""
协程和多线程的区别:
    1. 协程为单线程
    2. 协程由用户决定,在哪些地方交出控制权,切换到下一个任务
"""


import time
import random
import asyncio


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()
    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))
    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))
    #  创建任务就是直接放到事件循环中， 协程函数加上() 会返回协程对象， 不是会执行，所以任务列表中放置的是协程的对象
    await asyncio.sleep(10)
    # time.sleep(10)
    # 相当于一个IO阻塞的情况， 这种情况下可以直接跳转到其他的地方去执行
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)
#      如果有异常是否有返回   return_exceptions
#  gather和await 的效果一致



start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print(end - start)
