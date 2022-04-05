# 第 8 章： 函数 - 迭代器与生成器

# 迭代器有两个基本的方法：iter() 和 next()
import sys

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




def main():
    iter_func()


if __name__ == '__main__':
    main()
