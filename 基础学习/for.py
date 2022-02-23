# 推导式
def forFunc():
    # 从1 到 10  所有偶数的平方
    alist = []
    for i in range(1, 11):
        if i % 2 == 0:
            alist.append( i*i )
    print("从1 到 10  所有偶数的平方", alist)
    blist = [i*i for i in range(1, 11) if(i % 2) == 0]
    print("从1 到 10  所有偶数的平方", alist)

    class_names = ['PHP', 'Swift', 'Java', 'Python', 'Objective-C']
    z_num = {}
    for i in class_names:
        z_num[i] = 0
    print("转字典", z_num)
    z_num = {i:0 for i in class_names}
    print("转字典", z_num)

def main():
    forFunc()

if __name__ == '__main__':
    main()