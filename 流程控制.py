# 条件语句
'''
if expression:
    expr_true_suite
elif expression2:
    expr2_true_suite
else
    expr_false_suite

1.使用缩进而不是大括号来标记代码块边界，因此要特别注意 else 的悬挂问题。
2.单个 if 语句中的 expression 条件表达式可以通过布尔操作符 and , or 和 not 实现多重条件判断。
e.g.
'''
if 2 > 1 and not 2 > 3:
    print('Correct Judgement!')
# Correct Judgement!

# assert
'''
assert 这个关键词我们称之为“断言”，当这个关键词后边的条件为 False 时，程序自动崩溃并抛
出 AssertionError 的异常。
'''
my_list = ['lsgogroup']
my_list.pop(0)
assert len(my_list) > 0
# AssertionError

# while
'''
while 布尔表达式:
    代码块

1.while 语句最基本的形式包括一个位于顶部的布尔表达式，一个或多个属于 while 代码块的缩进语句
2.while 循环的代码块会一直循环执行，直到布尔表达式的值为布尔假
3.如果布尔表达式不带有 <、>、==、！=、in、not in 等运算符，仅仅给出数值之类的条件，也是可以的。当 while 后写
入一个非零整数时，视为真值，执行循环体；写入 0 时，视为假值，不执行循环体。也可以写入 str、list 或任何序
列，长度非零则视为真值，执行循环体；否则视为假值，不执行循环体。
'''

'''
while 布尔表达式:
    代码块
else:
    代码块
当 while 循环正常执行完的情况下，执行 else 输出，如果 while 循环中执行了跳出循环的语句，比如 break ，将不执
行 else 代码块的内容
'''

# for
'''
for 迭代变量 in 可迭代对象:
    代码块

1.for 循环是迭代循环，在Python中相当于一个通用的序列迭代器，可以遍历任何有序序列，如 str、list、tuple 等，也
可以遍历任何可迭代对象，如 dict 。
- for i in 'ILoveLSGO':

- member = ['张三', '李四', '刘德华', '刘六', '周润发']
    for each in member:

- for i in range(len(member)):

- dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key, value in dic.items():
for key in dic.keys():
for key in dic.values():
'''

'''
for 迭代变量 in 可迭代对象:
    代码块
else:
    代码块

1.当 for 循环正常执行完的情况下，执行 else 输出，如果 for 循环中执行了跳出循环的语句，比如 break ，将不执
行 else 代码块的内容，与 while - else 语句一样
'''

# range
'''
range([start,] stop[, step=1])

1.这个BIF（Built-in functions）有三个参数，其中用中括号括起来的两个表示这两个参数是可选的。
2. step=1 表示第三个参数的默认值是1。
3. range 这个BIF的作用是生成一个从 start 参数的值开始到 stop 参数的值结束的数字序列，该序列包含 start 的
值但不包含 stop 的值。

'''
for i in range(2, 9):  # 不包含9
    print(i)
# 2
# 3
# 4
# 5
# 6
# 7
# 8

for i in range(1, 10, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9

# enumerate
'''
enumerate(sequence, [start=0])

1. sequence -- 一个序列、迭代器或其他支持迭代对象。
2. start -- 下标起始位置。
3. 返回 enumerate(枚举) 对象


'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
lst = list(enumerate(seasons))
print(lst)
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
lst = list(enumerate(seasons, start=1))  # 下标从 1 开始
print(lst)
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# enumerate() 与 for 循环的结合使用
'''
for i, a in enumerate(A)
 do something with a

用 enumerate(A) 不仅返回了 A 中的元素，还顺便给该元素一个索引值 (默认从 0 开始)。此外，用
enumerate(A, j) 还可以确定索引起始值为 j
'''

# 流程终止
'''
1.break 语句可以跳出当前所在层的循环。
2.continue 终止本轮循环并开始下一轮循环。
3.pass 语句的意思是“不做任何事”，如果你在需要有语句的地方不写任何语句，那么解释器会提示出错，而 pass 语句就
是用来解决这些问题的。

'''
# 推导式
'''
[ expr for value in collection [if condition] ]

'''

# 列表推导式
x = [-4, -2, 0, 2, 4]
y = [a * 2 for a in x]
print(y)
# [-8, -4, 0, 4, 8]

x = [i ** 2 for i in range(1, 10)]
print(x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

x = [(i, i ** 2) for i in range(6)]
print(x)
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

x = [i for i in range(100) if (i % 2) != 0 and (i % 3) == 0]
print(x)
# [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]

a = [(i, j) for i in range(0, 3) for j in range(0, 3)]
print(a)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

x = [[i, j] for i in range(0, 3) for j in range(0, 3)]
print(x)
# [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
x[0][0] = 10
print(x)
# [[10, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

a = [(i, j) for i in range(0, 3) if i < 1 for j in range(0, 3) if j > 1]
print(a)
# [(0, 2)]

# 元组推导式
'''
( expr for value in collection [if condition] )

'''
a = (x for x in range(10))
print(a)
# <generator object <genexpr> at 0x0000025BE511CC48>
print(tuple(a))
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 字典推导式
'''
{ key_expr: value_expr for value in collection [if condition] }

'''
b = {i: i % 2 == 0 for i in range(10) if i % 3 == 0}
print(b)
# {0: True, 3: False, 6: True, 9: False}

# 集合推导式
'''
{ expr for value in collection [if condition] }

'''
c = {i for i in [1, 2, 3, 4, 5, 5, 6, 4, 3, 2, 1]}
print(c)
# {1, 2, 3, 4, 5, 6}

# 其它
d = 'i for i in "I Love Lsgogroup"'
print(d)
# i for i in "I Love Lsgogroup"
e = (i for i in range(10))
print(e)
# <generator object <genexpr> at 0x0000007A0B8D01B0>
print(next(e))  # 0
print(next(e))  # 1
for each in e:
    print(each, end=' ')
# 2 3 4 5 6 7 8 9
s = sum([i for i in range(101)])
print(s)  # 5050
s = sum((i for i in range(101)))
print(s)  # 5050
