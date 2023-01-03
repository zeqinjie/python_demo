
# 读取文件内容
def readfile(file_name='file.txt'):
    file = open(file_name)
    str = file.read()
    file.close()
    return str


# 写入文件内容
def writefile(file_name='file.txt', txt=''):
    file = open(file_name, 'w')
    file.write(txt)
    file.close()
    pass

if __name__ == "__main__":
    # 读取文件
    txt = readfile()
    print(f"读取文件内容: {txt}")
    txt = txt.replace('\"', '')
    txt = txt.replace(',', '')
    txt = txt.replace('{', '')
    txt = txt.replace('}', '')
    txt = txt.strip('\n')
    writefile(txt=txt)
    pass