def filter_func():
    oldlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newlist1 = list(filter(is_even_num, oldlist))
    print("过滤出奇数：", newlist1)
    newlist2 = list(filter(lambda x: x % 2 == 0, oldlist))
    print("过滤出偶数：", newlist2)


def map_func():
    oldlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newlist1 = list(map(lambda x: x * 2, oldlist))
    print("旧数组里的数 * 2 = ", newlist1)
    newlist2 = list(map(lambda x, y: x + 2, oldlist, newlist1))
    print("oldlist 与 newlist2 相加等于", newlist2)


# 获取基数
def is_even_num(n):
    return n % 2 == 1


def main():
    filter_func()
    map_func()


if __name__ == '__main__':
    main()
