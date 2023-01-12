
'''
迭代器

1. 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
2. 迭代器是一个可以记住遍历的位置的对象。
3. 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
4. 迭代器只能往前不会后退。
5. 字符串，列表或元组对象都可用于创建迭代器：


迭代器的方法:
1. 迭代器有两个基本的方法： iter() 和 next() 。
2. iter(object) 函数用来生成迭代器。
3. next(iterator[, default]) 返回迭代器的下一个项目。
4. iterator -- 可迭代对象
5. default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发
StopIteration 异常。
'''

STRING = 'lsgogroup'
for c in STRING:
    print(c, end=" ")
# lsgogroup

for c in iter(STRING):
    print(c, end="-")

links = {'B': '百度', 'A': '阿里', 'T': '腾讯'}
for each in links:
    print('%s -> %s' % (each, links[each]))

# B -> 百度
# A -> 阿里
# T -> 腾讯

for each in iter(links):
    print('%s -> %s' % (each, links[each]))


it = iter(links)
print(next(it))  # B
print(next(it))  # A
print(next(it))  # T
# print(next(it))  # StopIteration
it = iter(links)
while True:
    try:
        each = next(it)
    except StopIteration:
        print(each)
        break
# B
# A
# T

'''
把一个类作为一个迭代器使用需要在类中实现两个魔法方法 __iter__() 与 __next__() 。
1. __iter__(self) 定义当迭代容器中的元素的行为，返回一个特殊的迭代器对象， 这个迭代器对象实现了
__next__() 方法并通过 StopIteration 异常标识迭代的完成。
2. __next__() 返回下一个迭代器对象。
3. StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完
成指定循环次数后触发 StopIteration 异常来结束迭代。
'''


class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


fibs = Fibs(100)
for each in fibs:
    print(each, end=' ')
# 1 1 2 3 5 8 13 21 34 55 89
