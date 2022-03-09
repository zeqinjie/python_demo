# -*- coding: utf-8 -*-
# -*- author: zhengzeqin -*-
# -*- date: 2022-03-07 -*-

"""
Flutter 修改默认生成的 minSdkVersion 问题
flutter pub get 会自动生成 android 目录，但是如果要修改 build.gradle 文件里面的内容，需要每次都要手动改一下，很麻烦
解决办法
修改 flutter 自动生成的 build.gradle 的模板文件
模板文件路径: flutter_sdk/packages/flutter_tools/templates/module/android/host_app_common/app.tmpl/build.gradle.tmpl
py 解决思路: 通过脚本一键复制修改 flutter 配置模板
"""

import os
import sys
import getopt

# 定义 flutter 目标 android project build_gradle 配置的路径
_project_build_gradle_set_file = "/Users/zhengzeqin/flutter/packages/flutter_tools/templates/module/android/gradle/build.gradle.tmpl"
# 定义 flutter 目标 android app build_gradle 配置的路径
_app_build_gradle_set_file = "/Users/zhengzeqin/flutter/packages/flutter_tools/templates/module/android/host_app_common/app.tmpl/build.gradle.tmpl"

# 定义需要写入的 android project 根目录的 build_gradle 配置
_build_gradle_tmpl_for_project = "/build_gradle_tmpl_for_project.txt"

# 定义需要写入的 android app 目录的 build_gradle 配置
_build_gradle_tmpl_for_app = "/build_gradle_tmpl_for_app.txt"

# 读取文件内容
def readfile(file_name):
    file2 = open(file_name)
    str = file2.read()
    file2.close()
    return str


# 设置 build_gradle 的内容
def android_gradle_set():
    # 获取当前文件路径
    concurrent = os.path.abspath(os.path.dirname(__file__))
    read_file_path = concurrent + '/build_gradle_tmpl_for_project.txt'
    write_file_path = concurrent + '/build.gradle.tmpl'
    read_file = open(read_file_path, 'r')
    write_file = open(write_file_path, "w")

    s = read_file.read()
    w = write_file.write(s)

    read_file.close()
    write_file.close()

# 从文件路径中写入到目标文件
def set_build_gradle_file(read_file_path, write_file):
    read_file = open(read_file_path, 'r')
    write_file = open(write_file, "w")
    s = read_file.read()
    write_file.write(s)
    read_file.close()
    write_file.close()

# 获取当前文件夹的路径
def get_current_path():
    return os.path.abspath(os.path.dirname(__file__))

# 设置 app 的 file
def set_app_build_gradle_file():
    read_file_path = get_build_gradle_file(_build_gradle_tmpl_for_app)
    set_build_gradle_file(read_file_path, _app_build_gradle_set_file)

# 设置 project 根目录的 file
def set_pro_build_gradle_file():
    read_file_path = get_build_gradle_file(_build_gradle_tmpl_for_project)
    set_build_gradle_file(read_file_path, _project_build_gradle_set_file)

# 读取本地配置文件
def get_build_gradle_file(build_gradle_tmpl):
    concurrent = os.path.abspath(os.path.dirname(__file__))
    read_file_path = concurrent + build_gradle_tmpl
    return  read_file_path

# 通过本地文件配置路径修改 Android 项目的 build_gradle 配置
def set_android_build_gradle_params_files():
    set_pro_build_gradle_file()
    set_app_build_gradle_file()

# 通过参数配置路径修改 Android 项目的 build_gradle 配置
def set_android_build_gradle_argv_files():
    argv = sys.argv[1:]
    # android project build_gradle 配置的路径
    project_path = ""
    # android app build_gradle 配置的路径
    app_path = ""
    # 默认关闭
    is_close_bitcode = True
    try:
        opts, args = getopt.getopt(argv, "p:a:", ["project=", "app="])
    except getopt.GetoptError:
        print('flutter_android_gradle_set.py -p "项目路径"')
        sys.exit(2)

    print("opts ===>", opts)

    for opt, arg in opts:
        if opt in ["-p", "--project"]:
            project_path = arg
        if opt in ["-a", "--app"]:
            app_path = arg
    # 设置 project build gradle
    read_pro_file_path = get_build_gradle_file(_build_gradle_tmpl_for_project)
    set_build_gradle_file(read_pro_file_path, project_path)
    # 设置 app build gradle
    read_app_file_path = get_build_gradle_file(_build_gradle_tmpl_for_app)
    set_build_gradle_file(read_app_file_path, app_path)

if __name__ == "__main__":
    set_android_build_gradle_params_files()
    # set_android_build_gradle_argv_files()
    pass
