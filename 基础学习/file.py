
def file_func():
    # 写入文件
    writefile(txt = 'a.诸葛亮')

    # 读取文件
    print(f"读取文件内容: {readfile()}")

    # 增加内容
    appendfile(txt = '\nb.刘备')

    # 读取 1 行
    print("读取 1 行", readfileline())

    # 读取每行
    readfilelines()

    file6 = open('name.txt')
    readfilecurrent(file6, num=1)
    # 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移，   2 从文件结尾
    file6.seek(5, 0)
    readfilecurrent(file6, num=1)

    file6.close()

# 读取文件内容
def readfile(file_name = 'name.txt'):
    file2 = open(file_name)
    str = file2.read()
    file2.close()
    return str

# 写入文件内容
def writefile(file_name = 'name.txt', txt = ''):
    file1 = open(file_name, 'w')
    file1.write(txt)
    file1.close()

# 追加文件内容
def appendfile(file_name = 'name.txt', txt = ''):
    file1 = open(file_name, 'a')
    file1.write(txt)
    file1.close()

# 读取一行
def readfileline(file_name = 'name.txt'):
    file4 = open(file_name)
    str = file4.readline()
    file4.close()
    return str

# 读取每行
def readfilelines(file_name = 'name.txt'):
    file5 = open(file_name)
    print("====读取每行====")
    for line in file5.readlines():
        print(line)
        print("===============")
    file5.close()

# 打印当前位置，和读取个数
def readfilecurrent(file, num = 1):
    print('当前文件指针的位置 %s' % file.tell())
    print('当前读取到了一个字符，字符的内容是 %s' % file.read(num))
    print('当前文件指针的位置 %s' % file.tell())

def main():
    file_func()

if __name__ == '__main__':
    main()