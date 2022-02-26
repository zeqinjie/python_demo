# 推导式
def for_func():
    # 从1 到 10  所有偶数的平方
    alist = []
    for i in range(1, 11):
        if i % 2 == 0:
            alist.append( i*i )
    print("从1 到 10  所有偶数的平方：", alist)
    blist = [i*i for i in range(1, 11) if(i % 2) == 0]
    print("blist 价于上面 alist：", blist)

    # 数组 class_namse 转字典
    class_names = ['PHP', 'Swift', 'Java', 'Python', 'Objective-C']
    adict = {}
    for i in class_names:
        adict[i] = 0
    print("生成字典：", adict)
    bdict = {i: 0 for i in class_names}
    print("bdict 等价于上面 adict：", bdict)

def main():
    for_func()

if __name__ == '__main__':
    main()