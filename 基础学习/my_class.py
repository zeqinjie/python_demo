# 定义一个类
class Player:
    # 类变量
    class_pro = "类属性"

    # 构造函数及成员变量
    def __init__(self, name, hp, occu, age = 22):
        self.__name = name  # 私有变量 __ 修饰
        self.hp = hp
        self.occu = occu
        self.age = age

    def print_role(self):  # 定义一个方法
        print('%s: %s %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.__private_func()
        self.__name = newname


    def __private_func(self):
        print("这是私有方法")

    # 定义类方法
    @classmethod
    def class_func(cls):
        print(f"我是类方法：{cls.class_pro}")
        # print(f"类方法不能访问类变量：{cls.hp}")


class Monster:
    """定义怪物类"""

    def __init__(self, hp=100):
        self.hp = hp

    def printHP(self):
        print(f'我的血量：{self.hp}')

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')


# Animals 基础父类类 Monster
class Animals(Monster):
    """普通怪物"""

    def __init__(self, hp=10):
        super().__init__(hp)


# Boss 基础父类类 Monster
class Boss(Monster):
    """Boss类怪物"""

    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):
        print('我是怪物我怕谁')


# 类的使用
def test_class():
    p1 = Player("zhengzeqin", 1000, "superman", age=40)
    p1.updateName("github")
    p1.print_role()

    Player.class_func()

    a1 = Monster(200)
    a1.printHP()
    print(a1.hp)
    print(a1.run())
    a2 = Animals(1)
    print(a2.hp)
    print(a2.run())

    a3 = Boss(800)
    a3.whoami()

    print('a1的类型 %s' % type(a1))
    print('a2的类型 %s' % type(a2))
    print('a3的类型 %s' % type(a3))

    print(isinstance(a2, Monster))


# 类的使用-自定义with语句
class Foo:
    def __enter__(self):
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit called")
        print("exc_type :%s" % exc_type)
        print("exc_val :%s" % exc_val)
        print("exc_tb :%s" % exc_tb)


class Testwith(object):
    """
    with 包含了 __enter__ 和 __exit__ 方法
    """
    def __enter__(self):
        print('run now ')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit normal ')
        else:
            print('exit with exception')


# 测试 with 用法
def test_with():
    with Foo() as foo:
        print("hello python")
        a = 1 / 2
        print(f"hello end: {a}")

    with Testwith():
        print('test')
        raise NameError('Exception')


if __name__ == "__main__":
    test_class()
    # test_with()
