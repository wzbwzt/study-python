
'''
列表是有序集合，没有固定大小，能够保存任意数量任意类型的 Python 对象，语法为 [元素1, 元素2, ..., 元素n] 。
1. 关键点是「中括号 []」和「逗号 ,」
2. 中括号 把所有元素绑在一起
3. 逗号 将每个元素一一分开
4.由于list的元素可以是任何对象，因此列表中所保存的是对象的指针。即使保存一个简单的 [1,2,3] ，也有3个指针和3个
整数对象。
5.列表不像元组，列表内容可更改 (mutable)，因此附加 ( append , extend )、插入 ( insert )、删除 ( remove , pop ) 这些
操作都可以用在它身上。

'''
# 创建方式1:利用 range() 创建列表
x = list(range(1, 11, 2))
print(x, type(x))
# [1, 3, 5, 7, 9] <class 'list'>

# 创建方式2:利用推导式创建列表
x = [0] * 5
print(x, type(x))
# [0, 0, 0, 0, 0] <class 'list'>
x = [0 for i in range(5)]
print(x, type(x))
# [0, 0, 0, 0, 0] <class 'list'>


# 创建方式3:赋值创建
x = [2, 3, 4, 5, 6, 7]
print(x, type(x))
# [2, 3, 4, 5, 6, 7] <class 'list'>

# 创建一个3*4的list
x = [[0] * 3] * 4
print(x, type(x))
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] <class 'list'>
x[0][0] = 1  # 因为存的是指针
print(x, type(x))
# [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]] <class 'list'>

a = [0] * 3
x = [a] * 4
print(x, type(x))
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] <class 'list'>
x[0][0] = 1  # 因为x = [a] * 4 操作中，只是创建4个指向list的引用，所以一旦 a 改变， x 中4个 a 也会随之改变。
print(x, type(x))
# [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]] <class 'list'>

# 向列表中添加元素
'''
list.append(obj) 在列表末尾添加新的对象，只接受一个参数，参数可以是任何数据类型，被追加的元素在 list
中保持着原结构类型。
'''
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.append('Thursday')
print(x)
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Thursday']

x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# 此元素如果是一个 list，那么这个 list 将作为一个整体进行追加，注意 append() 和 extend() 的区别。
x.append(['Thursday', 'Sunday'])

print(x)
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ['Thursday', 'Sunday']]

'''
list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

'''
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.extend(['Thursday', 'Sunday'])
print(x)
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Thursday', 'Sunday']

'''
list.insert(index, obj) 在编号 index 位置前插入 obj 。

'''
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.insert(2, 'Sunday')
print(x)
# ['Monday', 'Tuesday', 'Sunday', 'Wednesday', 'Thursday', 'Friday']

# 删除列表中的元素
'''
list.remove(obj) 移除列表中某个值的第一个匹配项

'''
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.remove('Monday')
print(x)  # ['Tuesday', 'Wednesday', 'Thursday', 'Friday']

'''
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

'''
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y = x.pop()
print(y)  # Friday

'''
del var1[, var2 ……] 删除单个或多个对象。

如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；如果你要在删除元素后还能继续使用它，
就使用方法 pop() 。
'''
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
del x[0:2]
print(x)  # ['Wednesday', 'Thursday', 'Friday']

# 获取列表中的元素
'''
1. 通过元素的索引值，从列表获取单个元素，注意，列表索引值是从0开始的。(左闭右开)
2. 通过将索引指定为-1，可让Python返回最后一个列表元素，索引 -2 返回倒数第二个列表元素，以此类推。
3.切片的通用写法是 start : stop : step;以具体的 step 从编号 start 往编号 stop 切片。注意最后把 step 设为 -1，相当于将列表反向排列。
4.[:]复制列表中的所有元素（浅拷贝）。

'''

x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(x[0], type(x[0]))  # Monday <class 'str'>
print(x[-1], type(x[-1]))  # Friday <class 'str'>
print(x[-2], type(x[-2]))  # Thursday <class 'str'>

# 列表的常用操作符
'''
1. 等号操作符： ==
「等号 ==」，只有成员、成员位置都相同时才返回True。
2. 连接操作符 +
3. 重复操作符 *
和元组拼接一样， 列表拼接也有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。
4. 成员关系操作符 in 、 not in


将两个list相加，需要创建新的 list 对象，从而需要消耗额外的内存，特别是当 list 较大时，尽量不要使用 “+” 来添加list
'''

list1 = [123, 456]
list2 = [456, 123]
list3 = [123, 456]
print(list1 == list2)  # False
print(list1 == list3)  # True
list4 = list1 + list2  # extend()
print(list4)  # [123, 456, 456, 123]
list5 = list3 * 3
print(list5)  # [123, 456, 123, 456, 123, 456]
list3 *= 3
print(list3)  # [123, 456, 123, 456, 123, 456]
print(123 in list3)  # True
print(456 not in list3)  # False

# list其他方法
'''
list.count(obj) 统计某个元素在列表中出现的次数
'''

list1 = [123, 456] * 3
print(list1)  # [123, 456, 123, 456, 123, 456]
num = list1.count(123)
print(num)  # 3

'''
list.index(x[, start[, end]]) 从列表中找出某个值第一个匹配项的索引位置
'''
list1 = [123, 456] * 5
print(list1.index(123))  # 0
print(list1.index(123, 1))  # 2
print(list1.index(123, 3, 7))  # 4

'''
list.reverse() 反向列表中元素
'''
x = [123, 456, 789]
x.reverse()
print(x)  # [789, 456, 123]

'''
list.sort(key=None, reverse=False) 对原列表进行排序。j
1.key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，j
指定可迭代对象中的一个元素来进行排序。
2.reverse -- 排序规则，reverse = True降序，reverse = False升序（默认）。
3.该方法没有返回值，但是会对列表的对象进行排序
'''
x = [123, 456, 789, 213]
x.sort()
print(x)
# [123, 213, 456, 789]
x.sort(reverse=True)
print(x)
# [789, 456, 213, 123]
# 获取列表的第二个元素


def takeSecond(elem):
    return elem[1]


x = [(2, 2), (3, 4), (4, 1), (1, 3)]
x.sort(key=takeSecond)
print(x)
# [(4, 1), (2, 2), (1, 3), (3, 4)]
x.sort(key=lambda a: a[0])
print(x)
# [(1, 3), (2, 2), (3, 4), (4, 1)]
