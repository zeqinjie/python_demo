
def add_func1(num1, num2):
    return num1 + num2

# 闭包函数
def add_func2(num1):
    def add(num2):
        return num1 + num2
    return add

# 计算器, 这里用列表是
def counter_func(num1 = 0):
    cnt = [num1]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

def add_line(a, b):
    # def arg_y(x):
    #     return a*x+b
    # return arg_y
    # 同上
    return lambda x: a*x+b

def closure_func():
    re1 = add_func1(1, 2)
    print("re1 类型", type(re1), re1)
    re2 = add_func2(1)
    print("re2 类型", type(re2), re2(2))
    num1 = counter_func(5)
    print(num1())
    print(num1())
    print(num1())
    line1 = add_line(3, 5)
    line2 = add_line(5, 15)
    print(line1(10))
    print(line2(20))

def main():
    closure_func()

if __name__ == '__main__':
    main()