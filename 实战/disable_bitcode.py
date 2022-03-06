# -*- coding: utf-8 -*-
# -*- author: zhengzeqin -*-
# -*- date: 2022-03-01 -*-

# 关闭 Flutter 项目 bitcode 
# 需要安装依赖库 
# pip3 install pbxproj

import os
import getopt
from pbxproj import XcodeProject
import sys

# 定义项目 module 文件名
_module_names = ['tw591_salehouse']
# 项目的父目录
_file_path = "/Users/zhengzeqin/Desktop/GitLab/"
# flutter project.pbxpro
_flutter_pro = '/.ios/Runner.xcodeproj/project.pbxproj'


# 本地文件配置路径处理 bitcode
def handle_projects_bit_code():
    for module_name in _module_names:
        set_bit_code(_file_path, module_name)


# 设置 bitcode
def set_bit_code(file_path, module_name):
    path = file_path + module_name + _flutter_pro
    # print("当前项目路径：", path)
    set_bit_code_path(path)


# 设置 bitcode
def set_bit_code_path(path, is_close_bitcode=True):
    project = XcodeProject.load(path)
    bitcode_str = "NO"
    if not is_close_bitcode:
        bitcode_str = "YES"
    print(f"set_bit_code_path 当前项目路径：{path} bitcode_str: {bitcode_str}")
    set_bit_code_flag(project, bitcode_str, configuration_name="Debug")
    set_bit_code_flag(project, bitcode_str, configuration_name="Profile")
    set_bit_code_flag(project, bitcode_str, configuration_name="Release")
    project.save()


# 设置 bitcode 参数
def set_bit_code_flag(project, bitcode_str, target_name="Runner", configuration_name='Debug'):
    project.set_flags('ENABLE_BITCODE', bitcode_str, target_name=target_name, configuration_name=configuration_name)

# cd /Users/zhengzeqin/Desktop/GitLab/TWHouseScript; python disable_bitcode.py -p '/Users/zhengzeqin/Desktop/GitLab/tw591_salehouse' -s close
if __name__ == "__main__":
    # 本地文件配置路径处理 bitcode
    # handle_projects_bit_code()
    # 如果是 flutter 同级下配置可以这样读取 project.pbxproj 路径
    # current_path = os.path.abspath(os.curdir) + _flutter_pro
    # print(current_path)

    argv = sys.argv[1:]
    # 项目路径
    project_path = ""
    # 默认关闭
    is_close_bitcode = True
    try:
        opts, args = getopt.getopt(argv, "p:s:", ["path=", "switch="])
    except getopt.GetoptError:
        print('disable_bitcode.py -p "项目路径"')
        sys.exit(2)

    print("opts ===>", opts)

    for opt, arg in opts:
        if opt in ["-p", "--path"]:
            project_path = arg
            if len(project_path) == 0:
                print('请输入项目的地址')
                sys.exit('请输入项目的地址')
        if opt in ["-s", "--switch"]:
            if arg == "open":
                is_close_bitcode = False
            if arg == "close":
                is_close_bitcode = True

    # 获取需要修复项目的路径
    path = project_path + _flutter_pro
    # 设置 bitcode = false
    set_bit_code_path(path, is_close_bitcode)

    pass
