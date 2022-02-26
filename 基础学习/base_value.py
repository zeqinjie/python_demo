# https://www.readwithu.com/Article/codeSpecification/codeSpecification_first.html
# 2) 基本数据

""" 一）基本数据
整数、浮点数、字符串、布尔值
打印类型：type()
"""

# 整数
def num():
    int1 = 1 + 1
    int2 = 1 * 1
    print("整数：", int1, "和", int2)

# 浮点
def float():
    float1 = 0.1 * 3
    # 取整除的返回整数的部分
    float2 = 11 // 3
    print("整数：", float1, "和", float2)

# 布尔值
# 布尔值可以用 and、or 和 not  运算
def bool():
    isRun = True
    isFly = False
    if isRun:
        print("它会跑")
    if isRun and isFly:
        print("它既会跑也会飞")
    if not isFly:
        print("它不会飞")

def null():
    nullValue = None

# 类型转换
# 类型判断: type(var)
# 类型转换： int()、float()、str()、bool()
def base_vaule():
    num = 2
    moneyString = "100"
    money = int(moneyString)
    txt = "hello word"
    isError = True
    print("num:", num, "money:", money, "txt:", txt)
    print("isError type:", type(isError))
    print("money type:", type(money))

# 案例
def caculator():
    # 定义美元
    dollar = 100
    # 定义汇率
    exchange = 6.4696
    # 输出结果
    print('{dol}美元兑换的人民币数量为{yuan}'.format(dol=dollar, yuan=dollar * exchange))



""" 
含义是如果独立运行那么main( )方法就会被执行，如果作为模块导入就不会执行
"""
def main():
    # num()
    # float()
    # bool()
    # caculator()
    base_vaule()
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

