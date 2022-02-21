# set
def setFunc():
    set1 = set(['Java', 'OC', 'Swift', 'Swift'])
    print(set1)
    set1.add('Dart')
    print("添加 Dart:", set1)
    set1.remove('Swift')
    print("移除 Swift:", set1)
    # 交集 (求两个 set 集合中相同的元素)
    set2 = set(['Shell', 'Python', 'Ruby', 'Java'])
    set3 = set1 & set2
    print("求两个 set 集合中相同的元素:", set3)
    # 并集 （合并两个 set 集合的元素并去除重复的值）
    set4 = set1 | set2
    print("合并两个 set 集合的元素并去除重复的值:", set4)
    # 差集
    set5 = set1 - set2
    print("差集:", set5)


def main():
    setFunc()

if __name__ == '__main__':
    main()