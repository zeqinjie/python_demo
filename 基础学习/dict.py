# 字典
def dictFunc():
    dict1 = {'1': 'Java', '2': 'PHP', '3': 'Swift'}
    print(dict1)
    # 新增一个键值对
    dict1['4'] = 'Objctive-c'
    print("新增一个键值对:", dict1)
    # 修改键值对
    dict1['2'] = 'Dart'
    print("修改键值对:", dict1)
    # 通过 key 值，删除对应的元素
    del dict1['2']
    print("通过 key 值，删除对应的元素:", dict1)
    for key in dict1.keys():
        print("key is:", key, "value is:", dict1[key])
    # 删除字典中的所有元素
    dict1.clear()
    print("删除字典中的所有元素:", dict1)

def main():
    dictFunc()

if __name__ == '__main__':
    main()