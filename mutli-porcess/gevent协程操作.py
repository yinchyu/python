import os
import gevent
from gevent import monkey

import time
# monkey.patch_os()
# 向环境变量中添加值然后进行操作
#; monkey.patch_all()
'''
It seems that the gevent monkey-patching is being used.
Please set an environment variable with:
GEVENT_SUPPORT=True
to enable gevent support in the debugger.

 gevent 支持调试的工作依然没有找到问题所在，添加环境变量然后也没有解决问题， 执行选择不使用monkey 进行调试
'''
os.environ["GEVENT_SUPPORT"]="True"


def test1(n):
     for i in range(n):
         print(gevent.getcurrent(),i)
         gevent.sleep(0.1)
def test2(n):
     for i in range(n):
         print(gevent.getcurrent(),i)
         gevent.sleep(0.1)
def test3(n):
     for i in range(n):
         print(gevent.getcurrent(),i)
         gevent.sleep(0.1)


h1=gevent.spawn(test1,5)
h2=gevent.spawn(test2,5)
h3=gevent.spawn(test3,5)


h1.join()
h2.join()
h3.join()

# 整体加入join阻塞队列中
# gevent.joinall([gevent.spawn(test1,5),
# gevent.spawn(test1,5),
# gevent.spawn(test1,5)]
# )
