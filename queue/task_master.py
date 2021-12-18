import random, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


task_queue = queue.Queue()
result_queue = queue.Queue()


def task_q():
    return task_queue


def result_q():
    return result_queue


if __name__ == "__main__":

    QueueManager.register("get_task_queue", callable=task_q)
    QueueManager.register("get_result_queue", callable=result_q)
    # 通过分布式，需要对数据管道进行注册操作
    # ，Queue对象存储在task_master.py进程中
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b"abcd")
    manager.start()
    # 通過manager 來进行管理
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
