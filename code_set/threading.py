# -*- coding: utf-8 -*-

"""
threading的一些用法
"""

import threading
import time


def loop_1(i=1):
    print("我是loop_1, thread %s 正在执行 ..." % threading.current_thread().name)
    while i < 5:
        i += 1
        print("%s >>>> %i" % (threading.current_thread().name, i))
        time.sleep(1)

def loop_2(i=1):
    print("我是loop_2, thread %s 正在执行 ..." % threading.current_thread().name)
    while i < 5:
        i += 1
        print("%s >>>> %i" % (threading.current_thread().name, i))
        time.sleep(1)

def endless_loop():
    print("我是endless_loop, thread %s 正在执行 ..." % threading.current_thread().name)
    x = 0
    while True:
        x = x ^ 1


"""
1. GIL测试 -- 假设CPU核心数为N，启动N个线程同时执行死循环，查看CPU消耗
——————————————————————————————————————————————————————————————————————
"""
def GIL_verify():
    import multiprocessing

    N_CPU = multiprocessing.cpu_count()

    for i in range(N_CPU):
        print('正在启动第 %i 个线程' % i)
        t = threading.Thread(target=endless_loop, name='thread_%i' % i)
        t.start()
        t.join()


"""
2. 启动两个线程执行不同的任务
——————————————————————————————————————————————————————————————————————
"""
def thread_double():
    # 避免在 target 函数上传参
    t1 = threading.Thread(target=loop_1, name="线程1")
    t2 = threading.Thread(target=loop_2, name="线程2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()



