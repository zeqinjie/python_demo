
"""
Flutter 修改默认生成的 minSdkVersion 问题
flutter pub get 会自动生成 android 目录，但是如果要修改 build.gradle 文件里面的内容，需要每次都要手动改一下，很麻烦
解决办法
修改 flutter 自动生成的 build.gradle 的模板文件
模板文件路径: flutter_sdk/packages/flutter_tools/templates/module/android/host_app_common/app.tmpl/build.gradle.tmpl
py 解决思路: 通过脚本一键复制修改 flutter 配置模板
"""

import os
import getopt

# 定义 flutter 目标 android project build_gradle 配置的路径
_project_build_gradle_set_file_path = "/Users/addcn/flutter/packages/flutter_tools/templates/module/android/gradle/build.gradle.tmpl"
# 定义 flutter 目标 android app build_gradle 配置的路径
_app_build_gradle_set_file_path = "/Users/addcn/flutter/packages/flutter_tools/templates/module/android/host_app_common/app.tmpl/build.gradle.tmpl"

# 定义需要写入的 android project 根目录的 build_gradle 配置
_build_gradle_tmpl_for_project_path = "/build_gradle_tmpl_for_project.txt"

# 定义需要写入的 android app 目录的 build_gradle 配置
_build_gradle_tmpl_for_app_path = "/build_gradle_tmpl_for_app.txt"

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
def set_build_gradle_file(read_file_path, write_file_path):
    read_file = open(read_file_path, 'r')
    write_file = open(write_file_path, "w")
    s = read_file.read()
    w = write_file.write(s)
    read_file.close()
    write_file.close()

# 获取当前文件夹的路径
def get_current_path():
    return os.path.abspath(os.path.dirname(__file__))

# 设置 app 的 file
def set_app_build_gradle_file():
    concurrent = os.path.abspath(os.path.dirname(__file__))
    read_file_path = concurrent + _build_gradle_tmpl_for_app_path
    # check_path = concurrent + "/app"
    # write_file_path = concurrent + "/build.gradle.tmpl"
    # mkdir(check_path)
    set_build_gradle_file(read_file_path, _app_build_gradle_set_file_path)

# 设置 project 根目录的 file
def set_pro_build_gradle_file():
    concurrent = os.path.abspath(os.path.dirname(__file__))
    read_file_path = concurrent + _build_gradle_tmpl_for_project_path
    # write_file_path = concurrent + "/build.gradle.tmpl"
    set_build_gradle_file(read_file_path, _project_build_gradle_set_file_path)


if __name__ == "__main__":
    # 修改 Android 项目的 build_gradle 项目
    set_pro_build_gradle_file()
    set_app_build_gradle_file()

