# 3) 序列
""" 二）序列: 字符串、列表（同数组）、元组
● 都可以通过索引得到每一个元素
● 默认索引值总是从零开始
● 可以通过切片的方法得到一个范围内的元素的集合
● 有很多共同的操作符(重复操作符、拼接操作符、成员关系操作符)
● Python针对序列有非常多的内置函数：list(), tuple(), str(), len(), max(), min(), sum(), sorted(), reversed(),enumerate(), zip()等等
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

# 字符串
def string():
    chinese_zodiac1 = "鼠牛虎兔龙蛇"
    chinese_zodiac2 = "马羊猴鸡狗猪"
    chinese_zodiac = chinese_zodiac1 + chinese_zodiac2
    print("chinese_zodiac 输出结果：", chinese_zodiac)
    print("chinese_zodiac * 2 输出结果：", chinese_zodiac * 2)
    print("chinese_zodiac[1] 输出结果：", chinese_zodiac[1])
    print("chinese_zodiac[1:4] 输出结果：", chinese_zodiac[1:4])
    if ("牛" in chinese_zodiac):
        print("牛 在变量 chinese_zodiac 中")
    else:
        print("牛 不在变量 chinese_zodiac 中")

    if ("猫" not in chinese_zodiac):
        print("猫 不在变量 chinese_zodiac 中")
    else:
        print("M 在变量 chinese_zodiac 中")
    print(r'\n')
    print(R'\n')

# 字符串格式化
def string_format():
    chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
    # Python 字符串格式化:
    chinese_zodiac_str = chinese_zodiac[2:5]
    print("截取下标 2 到下标 4: %s 共: %d 个数" % (chinese_zodiac_str, len(chinese_zodiac_str)))
    print("chinese_zodiac 输出结果：", chinese_zodiac)

# 字符串函数
def string_func():
    name = "zhengzeqin"
    print("首字母大写:", name.capitalize())
    # 长度
    print("原字符串居中,并使用 * 填充至长度 12 的新字符串:", name.center(12, "*"))
    pass

# 列表
def list():
    class_names = ['PHP', 'Swift', 'Java', 'Python', 'Objective-C']
    print("class_names 个数:", len(class_names))
    print("下标 1 到 3", class_names[1:4])
    if 'PHP' in class_names:
        print("php 在 class_names 中")
    else:
        print("php 不在 class_names 中")
    print("class_names 倒数第 2 个: ", class_names[-2])
    print("下标 3: ", class_names[3])
    print("从 0 读取到下标 2: ", class_names[:3])
    print("从下标 1 开始读取: ", class_names[1:])

# 列表的函数
def list_fun():
    class_names = ['PHP', 'Swift', 'Java', 'Python', 'Objective-C']
    class_names.append("Dart")
    print(class_names)
    print("Python 的下标：", class_names.index("Python"))
    del class_names

# 元组
def tuple():
    tuple1 = ('PHP', 'Swift', 'Java',  1, 2, 3)
    tuple2 = 'Python', 'Objective-C', 4, 5
    print("tuple1 取下标 0:", tuple1[1])
    print("tuple1 + tuple2 :", tuple1 + tuple2)
    # 元组内 list 的值被修改了，元组结果也变化
    list = [1, 2, 3]
    tuple3 = (tuple2, list)
    print(tuple3)
    list[0] = 4
    print(tuple3)
    # 删除元组
    del tuple2



def main():
    # string()
    # string_format()
    # string_func()
    # list()
    # listFun()
    # tuple()
    # sequece()
    pass

if __name__ == '__main__':
    main()