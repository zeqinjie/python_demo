# 第 12 章: 多线程编程

import threading
import time
from threading import current_thread


# 定义线程方法
def my_thread(arg1, arg2):
    print(threading.currentThread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    print(threading.currentThread().getName(), 'end')


# 测试
def test_func():
    for i in range(1, 6):
        t1 = threading.Thread(target=my_thread, args=(i, i + 1))
        t1.start()
    print(current_thread().getName(), 'end')


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


def test_func2():
    t1 = MyThread()
    t1.start()
    t1.join()
    print(current_thread().getName(), 'end')


# test_func()
test_func2()
