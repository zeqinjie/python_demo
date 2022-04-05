# 第 8 章：函数 - 装饰器的定义

import time


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间是 %s 秒 " % (stop_time - start_time))

    return wrapper


@timmer
def i_can_sleep():
    time.sleep(3)


def tips(func):
    def nei(a, b):
        print('start')
        func(a, b)
        print('stop')
        return 'I am here!!!!'

    return nei


@tips
def add(a, b):
    print(a + b)


def new_tips(argv):
    def tips(func):
        def nei(a, b):
            start_time = time.time()
            # 这里加个变量接收返回值
            result = func(a, b)
            end_time = time.time()
            print('%s 运行时间: %s ' % (argv, end_time - start_time))
            # 这里再返回
            return result

        return nei

    return tips


@new_tips('sum_model')
def sum(a, b):
    return a + b


@new_tips('sub_model')
def sub(a, b):
    return a - b


def main():
    i_can_sleep()
    print(add(4, 5))
    print('求和 ', sum(3, 4))
    print('求差', (sub(7, 4)))


if __name__ == '__main__':
    main()
