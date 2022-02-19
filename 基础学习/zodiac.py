# https://www.readwithu.com/Article/codeSpecification/codeSpecification_first.html


""" 一）基本数据
整数、浮点数、字符串、布尔值
打印类型：type()
"""
def baseVaule():
    num = 2
    money = 1.0
    txt = "hello word"
    isError = True
    print("num:", num, "money:", money, "txt:", txt)
    print("is:", type(isError))

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

""" 三）基本数据
整数、浮点数、字符串、布尔值
打印类型：type()
"""
def tiao():
    zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
                   u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
    zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
                   (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

    (month, day) = (2, 15)

    zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)

    # print(list(zodiac_day))

    zodiac_len = len(list(zodiac_day)) % 12

    print(zodiac_name[zodiac_len])

    # 用户输入月份和日期
    int_month = int(input('请输入月份：'))
    int_day = int(input('请输入日期：'))

    print(type(int_month))

    # for 语句
    for zd_num in range(len(zodiac_days)):
        if zodiac_days[zd_num] >= (int_month, int_day):
            print(zodiac_name[zd_num])
            break
        elif int_month == 12 and int_day > 23:
            print(zodiac_name[0])
            break



""" 
含义是如果独立运行那么main( )方法就会被执行，如果作为模块导入就不会执行
"""
def main():
    # baseVaule()
    sequece()
    print('this message is from main function')

""" 
 1、当独立运行可以加 main 入口函数，主动调用
 2、py 中函数是定义在调用前
 3、作为 module import 话，则不会主动调用 mian 函数
 4、这块定义一般放最后，否则函数之间访问也有了先定义后调用的顺序
 5、py 中没有括号，都是看缩进
"""
if __name__ == '__main__':
    main()
    print(__name__)

# main()