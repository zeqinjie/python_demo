# set
def setFunc():
    set1 = set(['Java', 'OC', 'Swift', 'Swift'])
    print(set1)
    set1.add('Dart')
    print("添加 Dart:", set1)
    set1.remove('Swift')
    print("移除 Swift:", set1)
    set2 = set(['Shell', 'Python', 'Ruby', 'Java'])
    # 交集 & : set1&set2，返回一个新的集合，包括同时在集合 set1 和 set2 中的共同元素。
    set3 = set1 & set2
    print("交集 求两个 set 集合中相同的元素:", set3)
    # 并集 | : set1|set2，返回一个新的集合，包括集合 set1 和 set2 中所有元素。
    set4 = set1 | set2
    print("并集 包括集合 set1 和 set2 中所有元素:", set4)
    # 差集 - : set1-set2，返回一个新的集合,包括在集合 set1 中但不在集合 set2 中的元素
    set5 = set1 - set2
    print("差集 包括在集合 set1 中但不在集合 set2 中的元素:", set5)
    # 补集 ^ : set1^set2，返回一个新的集合，包括集合 set1 和 set2 的非共同元素。
    set6 = set1 - set2
    print("差集 集合 set1 和 set2 的非共同元素:", set6)

def main():
    setFunc()

if __name__ == '__main__':
    main()