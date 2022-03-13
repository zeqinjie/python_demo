def add(num1, num2):
    "求两数相加值"
    return num1 + num2


def reduce(num1, num2):
    "求两数相减值"
    return num1 - num2


def multiply(num1, num2):
    """求两数相乘值"""
    return num1 * num2


# 补充默认值
def divide(num1=4, num2=2):
    "求两数相除值"
    return num1 / num2


# 返回多个值
def getValues(num1, num2):
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a


# 不定长函数
def print_info(arg1, *vartuple):
    print("zeqin 输出: ", arg1)
    for var in vartuple:
        print(",", var)
    return None


# 打印用户信息
def print_user_info(name, *, age, height=200):
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('体重：{}'.format(height))


# 不可以变
def unchange(num):
    num = num + 1
    print("unchange 里 num 的值", num)


# 可以变
def change(list):
    list.append(123)
    print("change 里 list 的值", list)


# lambda 匿名函数
def lambda_func():
    sum = lambda num1, num2: num1 + num2;
    print(sum(1, 2))


def test_func():
    a = 100
    b = 20
    print("a+b = ", add(a, b))
    print("a-b = ", reduce(a, b))
    print("axb = ", multiply(a, b))
    print("a/b = ", divide(a, b))

    # 取默认值， 注意第一个默认值可以省略形参名
    print("b 取默认值 = ", divide(num1=20))
    print("a 取默认值 = ", divide(num2=100))

    # 返回多个值，注意一次接受多个返回值的数据类型就是元组
    num1, num2 = getValues(10, 2)
    tuple1 = getValues(10, 2)
    print("求商与余数", num1, num2)
    print("求商与余数的元组", tuple1)

    # 不定长参数
    print_info("我叫", "zhenzeqin", "age = 20", "height = 100kg")

    # print_user_info("zhengzeqin", 20, 100) # 报错 参数是 * 号后的不能省略参数名
    print_user_info("zhengzeqin", age=20, height=100)

    # 不可变
    num11 = 100
    unchange(num11)
    print("unchange 外 num 的值", num11)

    # 可以变
    list11 = [1, 2, 3]
    change(list11)
    print("change 外 list 的值", list11)

    # lambda 匿名函数
    lambda_func()


def main():
    test_func()


if __name__ == '__main__':
    main()
