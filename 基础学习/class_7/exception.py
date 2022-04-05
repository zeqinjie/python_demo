# 第 7 章： 错误与异常

i = j

print())


a='123'
print(a[3])

d = {'a':1 ,'b':2}
print(d['c'])


year = int(input('input year:'))

try:
    year = int(input('input year:'))
except ValueError:
    print('年份要输入数字')

a=123
a.append()

except (ValueError, AttributeError, KeyError)


try:
    print(1/'a')
except Exception as e:
    print(' %s' %e)

try:
    raise NameError('helloError')
except NameError:
    print('my custom error')


try:
    a = open('../class_6/name.txt')
except Exception as e:
    print(e)

finally:
    a.close()



