import os
import sys
import getopt
import ds_opencc

# 创建 OpenCC 实例
cc = ds_opencc.OpenCC('s2tw.json')


def is_comment(line):
    # 判断是否是 Dart 文件中的注释
    return line.strip().startswith('//') or line.strip().startswith('/*') or line.strip().endswith('*/') or line.strip().startswith('*')


def convert_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    converted_lines = []
    in_block_comment = False

    for line in lines:
        if '/*' in line and '*/' not in line:
            in_block_comment = True
        elif '*/' in line:
            in_block_comment = False

        if in_block_comment or is_comment(line):
            converted_lines.append(line)
        else:
            converted_lines.append(cc.convert(line))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(converted_lines)


def convert_dart_files_in_directory(directory):
    print(f'Converting Dart files in {directory}...')
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.dart'):
                convert_file(os.path.join(root, file))

# python chinese_convert.py -p '/Users/zhengzeqin/Desktop/GitLab/tw591_xxx'
if __name__ == '__main__':
    argv = sys.argv[1:]
    # 项目路径
    project_path = ""
    try:
        opts, args = getopt.getopt(argv, "p:", ["path="])
    except getopt.GetoptError:
        print('convert.py -p "项目路径"')
        sys.exit(2)

    print("opts ===>", opts)

    for opt, arg in opts:
        if opt in ["-p", "--path"]:
            project_path = arg
            if len(project_path) == 0:
                print('请输入项目的地址')
                sys.exit('请输入项目的地址')

    # 获取需要修复项目的路径
    if len(project_path) == 0:
        current_directory = os.path.dirname(os.path.abspath(__file__))
    else:
        current_directory = project_path
    print(f'current_directory: {current_directory}')
    convert_dart_files_in_directory(current_directory)
