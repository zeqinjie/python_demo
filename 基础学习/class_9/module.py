# 第 9 章: 模块

# 一般的导入模块的方式
import set
# 导入模块使用别名 as
import iter_and_yield as my_yield
# 导入模块的部分方法
from filter_and_map import filter_func, map_func
# 导入模块的所有内容
from 基础学习.class_5.dict import *

if __name__ == "__main__":
    # 一般使用情况
    set.set_func()

    # 使用别名 as
    my_yield.iter_func()

    # 使用 from 方式
    filter_func()
    map_func()

    # 导入模块的所有内容
    dict_func()
