
# 迭代器
# 迭代器有两个基本的方法：iter() 和 next()
import sys

# for 循环输出每个值
def for_func():
    class_names = ['PHP', 'Swift', 'Java', 'Python', 'Objective-C']
    for name in class_names:
	    print("class name:", name)
    for char in 'zhengzeqin':
        print(char, end=' ')

# 迭代器
def iter_func():
    class_names1 = ['PHP', 'Swift', 'Java']
    iter1 = iter(class_names1)
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    try:
        print(next(iter1))
    except Exception as e:
        print("捕获异常", e)
    # 也可以通过该 for 直接遍历，不过注意如果已执行完 next() 那下面就不会输出任何值了
    for x in iter1:
        print(x, end=" ")

    class_names2 = ['Python', 'Shell', 'Ruby']
    iter2 = iter(class_names2)
    while True:
        try:
            print(next(iter2))
        except StopIteration:
            print("异常抛出：exit")
            sys.exit()

# 生成器
def yield_func():
    print("------实现支持步长值为浮点的 range：------")
    for value in frange(10, 20, 0.5):
        print(value, end=',')

    print("\n------杨辉三角形生成器：------")
    n = 0
    for t in triangles(10):
        print(t)
        n = n + 1
        if n == 10:
            break

    print("\n------斐波那契生成器：------")
    # f 是一个迭代器，由生成器返回生成
    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=",")
        except StopIteration:
            sys.exit()


# 实现支持步长值为浮点的 range
def frange(start,stop,step):
    x = start
    while x < stop:
        yield x
        x +=step

# 杨辉三角形
def triangles(n):
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range (len(L))]

 # 生成器函数 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

def main():
    # for_func()
    # iter_func()
    yield_func()


if __name__ == '__main__':
    main()