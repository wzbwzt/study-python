# 表示注释，作用于整行
print("Hello world")


# 多行注释
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''
print("Hello china")
"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号
这是多行注释，用三个双引号
"""
print("hello china")

'''
运算符
+ 加 1+1
- 减 2-1
* 乘 3*4
/ 除 3/4
// 整除（地板除） 3//4
% 取余 3%4
** 幂 2**3
'''
print(3 % 2)  # 1
print(11 / 3)  # 3.6666666666666665
print(11 // 3)  # 3
print(2 ** 3)  # 8

'''
比较运算符
> 大于 2>1
>= 大于等于 4>=2
< 小于 1>2
<= 小于等于 2<=5
== 等于 3==3
!= 不等于 3!=5
'''

print(1 > 3)  # False
print(2 < 3)  # True
print(1 == 1)  # True
print(1 != 1)  # False

'''
逻辑运算符
and 与 (2>1) and (3>7)
or 或 (1>3) or (2<9)
not 非 not(2>1)

'''
print((3 > 2) and (3 < 5))  # True
print((1 > 3) and (2 < 1))  # False
print((1 > 3) or (3 < 5))  # True

'''
位运算符
~ 按位取反 ~4
& 按位与 4 & 5
| 按位或 4 | 5
^ 按位异或 4 ^ 5
<< 左移 4 << 2，表示整数 4 按位左移 2 位
>> 右移 4 >> 2，表示整数 4 按位右移 2 位
位运算是将左边的数的二进制左/右移指定位数

'''
# 三元运算符
x, y = 4, 5
if x < y:
    small = x
else:
    small = y
print(small)  # 4
# 写成一条语句
x, y = 4, 5
small = x if x < y else y
print(small)  # 4

'''
is 是 'hello' is 'hello'
not is 不是 3 is not 5
in 存在 5 in [1, 2, 3, 4, 5]
not in 不存在 2 not in [1, 2, 3, 4, 5]

'''

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
if 'A' in letters:
    print('A' + ' exists')
if 'h' not in letters:
    print('h' + ' not exists')
# A exists
# h not exists

"""
1. 假如比较的两个变量，指向的都是地址不可变的类型（str等），那么is，is not 和 ==，！= 是完全等价的。
is, is not 对比的是两个变量的内存地址
2. 假如对比的两个变量，指向的是地址可变的类型（list，dict，tuple等），则两者是有区别的
==, != 对比的是两个变量的值
"""

a = "hello"
b = "hello"
print(a is b, a == b)
# True True

a = ["hello"]
b = ["hello"]
print(a is b, a == b)
# False True

"""
运算符的优先级
1. 一元运算符优于二元运算符。如正负号。
2. 先算术运算，后移位运算，最后位运算。例如 1 << 3 + 2 & 7等价于 (1 << (3 + 2)) & 7
3. 逻辑运算最后结合

"""

# 变量和赋值

"""
1. 在使用变量之前，需要对其先赋值。
2. 变量名可以包括字母、数字、下划线、但变量名不能以数字开头。
3. Python 变量名是大小写敏感的，foo != Foo。
"""

# 数据类型与转换
'''
int 整型 - 876, 10
float 浮点型 3.149, 11.11
bool 布尔型 True, False
'''
a = 1031
print(a, type(a))
# 1031 <class 'int'>


# Python 里面万物皆对象（object），整型也不例外，只要是对象，就有相应的属性 （attributes） 和方法（methods）。

# 布尔 (boolean) 型变量只能取两个值， True 和 False 。当把布尔变量用在数字运算中，用 1 和 0 代表 True 和False
print(True + True)  # 2
print(True + False)  # 1
print(True * False)  # 0

'''
除了直接给变量赋值 True 和 False ，还可以用 bool(X) 来创建变量，其中 X 可以是
1. 基本类型：整型、浮点型、布尔型
2. 容器类型：字符、元组、列表、字典和集合
bool 作用在容器类型变量： X 只要不是空的变量， bool(X) 就是 True ，其余就是 False 。

'''
print(type(0), bool(0), bool(1))
# <class 'int'> False True
print(type(10.31), bool(0.00), bool(10.31))
# <class 'float'> False True
print(type(True), bool(False), bool(True))
# <class 'bool'> False True

print(type(''), bool(''), bool('python'))
# <class 'str'> False True
print(type(()), bool(()), bool((10,)))
# <class 'tuple'> False True
print(type([]), bool([]), bool([1, 2]))
# <class 'list'> False True
print(type({}), bool({}), bool({'a': 1, 'b': 2}))
# <class 'dict'> False True
print(type(set()), bool(set()), bool({1, 2}))
# <class 'set'> False True

# 要判断两个类型是否相同推荐使用 isinstance()
print(isinstance(1, int))  # True
print(isinstance(5.2, float))  # True
print(isinstance(True, bool))  # True
print(isinstance('5.2', str))  # True

'''
类型转换
1. 转换为整型 int(x, base=10)
2. 转换为字符串 str(object='')
3. 转换为浮点型 float(x)
'''
print(int('520'))  # 520
print(int(520.52))  # 520
print(float('520.52'))  # 520.52
print(float(520))  # 520.0
print(str(10 + 10))  # 20
print(str(10.1 + 5.2))  # 15.3
