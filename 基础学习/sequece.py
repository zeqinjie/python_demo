# 3) 序列

""" 二）序列: 字符串、列表（同数组）、元组、字典
"""
def sequece():
    a = [1, 2, 3, 4, 5]
    b = [6, 7]
    c = a + b
    print(c)
    d = a * 3
    print(d)
    a.append(6)
    print(a)
    a.remove(3)
    print(a)
    # 取下标 0，的3 个联系
    print(a[0:3])
    # 取最好 负数倒数着数
    print(a[-1])
    if 1 in a: # not in
        print("a 序列里有 1 ")
    else:
        print("a 序列没有 1 ")

