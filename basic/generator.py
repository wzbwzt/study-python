

'''
生成器

1. 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
2. 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
3. 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下
一次执行 next() 方法时从当前位置继续运行。
4. 调用一个生成器函数，返回的是一个迭代器对象。


得到生成器的方式有两种：
1.生成器函数 yield:
2.生成器表达式:

生成器函数 yield:
1.yield把函数变成了生成器（生成器就是迭代器）。
2.为函数封装好了__iter__和__next__方法，把函数的执行结果做成了迭代器。
3.遵循迭代器的取值方式 — obj.__next__()，触发的是函数的执行。函数暂停与继续执行的状态都是由yield保存的。



'''


def myGen():
    print('生成器执行！')
    yield 1
    yield 2


myG = myGen()
print(next(myG))
# 生成器执行！
# 1
print(next(myG))  # 2
# print(next(myG))  # StopIteration
myG = myGen()
for each in myG:
    print(each)
# 生成器执行！
# 1
# 2


def libs(n):
    a = 0
    b = 1
    while a < n:
        a, b = b, a + b
    if a > n:
        return
    yield a


for each in libs(100):
    print(each, end=' ')
# 1 1 2 3 5 8 13 21 34 55 89


'''
生成器表达式:
第二种自造迭代器的方法

列表推导式:[i for i in range(10)],得到一个元素数量较小的列表是非常方便的，但是如果要创建一个元素数量巨大的列表，就不那么友好了。
这个时候只要把[]换成()就把列表推导式 变成了生成器表达式，得到的就是一个生成器对象
(i for i in range(10))
'''
for i in (i for i in range(10)):
    print(i)
