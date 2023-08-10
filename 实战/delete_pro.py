import os
import sys
import datetime
import shutil

# # 获取命令行参数作为目标文件夹的路径
# target_folder = sys.argv[1]

# # 获取当前日期并减去两个月
# two_months_ago = datetime.datetime.now() - datetime.timedelta(days=60)

# # 遍历目标文件夹中的所有文件
# for root, dirs, files in os.walk(target_folder):
#     for file in files:
#         # 获取文件的创建日期
#         file_path = os.path.join(root, file)
#         created_date = datetime.datetime.fromtimestamp(
#             os.path.getctime(file_path))

#         # 如果文件创建日期早于两个月前，则删除该文件
#         if created_date < two_months_ago:
#             os.remove(file_path)


# 获取命令行参数作为目标文件夹的路径
target_folder = sys.argv[1]

# 获取当前日期并减去两个月
two_months_ago = datetime.datetime.now() - datetime.timedelta(days=60)

# 遍历目标文件夹中的所有文件夹
for root, dirs, files in os.walk(target_folder):
    for dir in dirs:
        # 获取文件夹的创建日期
        dir_path = os.path.join(root, dir)
        created_date = datetime.datetime.fromtimestamp(
            os.path.getctime(dir_path))

        # 如果文件夹创建日期早于两个月前，则删除该文件夹及其所有内容
        if created_date < two_months_ago:
            shutil.rmtree(dir_path)
