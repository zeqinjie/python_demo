# 字典
def dict():
    dict1 = {'1': 'Java', '2': 'PHP', '3': 'Swift'}
    print(dict1)
    # 新增一个键值对
    dict1['4'] = 'Objctive-c'
    print(dict1)
    # 修改键值对
    dict1['2'] = 'Dart'
    print(dict1)
    # 通过 key 值，删除对应的元素
    del dict1['2']
    print(dict1)
    # 删除字典中的所有元素
    dict1.clear()
    print(dict1)

def main():
    dict()

if __name__ == '__main__':
    main()