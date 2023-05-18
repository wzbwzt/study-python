
# 函数
'''
1. 函数以 def 关键词开头，后接函数名和圆括号()。
2. 函数执行的代码以冒号起始，并且缩进。
3. return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None 。

def functionname(parameters):
 "函数_文档字符串"
 function_suite
 return [expression]
'''


from functools import reduce


def add(a, b):
    print(a + b)


add(1, 2)  # 3
add([1, 2, 3], [4, 5, 6])  # [1, 2, 3, 4, 5, 6]

'''
函数参数
1. 位置参数 (positional argument)
2. 默认参数 (default argument)
3. 可变参数 (variable argument)
4. 关键字参数 (keyword argument)
5. 命名关键字参数 (name keyword argument)
6. 参数组合
'''
# 位置参数
'''
def functionname(arg1):
 "函数_文档字符串"
 function_suite
 return [expression]

arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定

注意事项：
位置参数在定义时就进行了初始化一次;
例如下面，name_list并不会在每次调用foo()时执行name_list=[]

'''


def foo(name, name_list=[]):
    name_list.append(name)
    print(name_list)


foo("Alex")
foo("Rain")
# 输出：
# ["Alex"]
# ["Alex", "Rain"]

# 默认参数
'''
def functionname(arg1, arg2=v):
 "函数_文档字符串"
 function_suite
 return [expression]

1.arg2 = v - 默认参数 = 默认值，调用函数时，默认参数的值如果没有传入，则被认为是默认值。
2.默认参数一定要放在位置参数后面，不然程序会报错
3.允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
'''
# 可变参数
'''
def functionname(arg1, arg2=v, *args):
 "函数_文档字符串"
 function_suite
 return [expression]

1.*args - 可变参数，可以是从零个到任意个，自动组装成元组。
2. 加了星号（*）的变量名会存放所有未命名的变量参数。
3.位置参数、默认参数、*args同时出现时，*args必须放在位置参数后面，因为*args本生就i相当于一组位置参数

可变参数允许传入零个到任意个参数，它们在函数调用时自动组装为一个元组 (tuple)。
'''


def printinfo(arg1, *args):
    print(arg1)
    for var in args:
        print(var)


printinfo(10)  # 10
printinfo(70, 60, 50)
# 70
# 60
# 50

# 关键字参数
'''
def functionname(arg1, arg2=v, *args, **kw):
 "函数_文档字符串"
 function_suite
 return [expression]

1.**kw - 关键字参数，可以是从零个到任意个，自动组装成字典。
2.** 的作用是按关键字传值多余的那些值塞到kwargs的字典里。
3.**kwargs应该放在最后。

关键字参数允许传入零个到任意个参数，它们在函数内部自动组装为一个字典 (dict)。
'''


def printinfo(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)


printinfo(70, 60, 50)
# 70
# (60, 50)
# {}
printinfo(70, 60, 50, a=1, b=2)
# 70
# (60, 50)
# {'a': 1, 'b': 2}

# 命名关键字参数
'''
def functionname(arg1, arg2=v, *args, *, nkw, **kw):
 "函数_文档字符串"
 function_suite
 return [expression]


1.*, nkw - 命名关键字参数，用户想要输入的关键字参数，定义方式是在nkw 前面加个分隔符 *。
2. 如果要限制关键字参数的名字，就可以用「命名关键字参数」
3. 使用命名关键字参数时，要特别注意不能缺少参数名。
'''


def printinfo(arg1, *, nkw, **kwargs):
    print(arg1)
    print(nkw)
    print(kwargs)


printinfo(70, nkw=10, a=1, b=2)
# 70
# 10
# {'a': 1, 'b': 2}
# printinfo(70, 10, a=1, b=2)#没有写参数名 nwk ，因此 10 被当成「位置参数」，而原函数只有 1 个位置函数，现在调用了 2 个，因此程序会报错。
# TypeError: printinfo() takes 1 positional argument but 2 were given

# 参数组合
'''
可以用位置参数、默认参数、可变参数、命名关键字参数和关键字参数，这 5 种参数中的 4 个都
可以一起使用，但是注意，参数定义的顺序必须是：
1. 位置参数、默认参数、可变参数和关键字参数。
2. 位置参数、默认参数、命名关键字参数和关键字参数。

要注意定义可变参数和关键字参数的语法：
1. *args 是可变参数， args 接收的是一个 tuple
2. **kw 是关键字参数， kw 接收的是一个 dict

命名关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。定义命名关键字参数不要忘了写分隔符
* ，否则定义的是位置参数。

警告：虽然可以组合多达 5 种参数，但不要同时使用太多的组合，否则函数很难懂。
'''


'''
变量作用域

内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了
'''


def discounts(price, rate):
    final_price = price * rate
    return final_price


old_price = float(input('请输入原价:'))  # 98
rate = float(input('请输入折扣率:'))  # 0.9
new_price = discounts(old_price, rate)
print('打折后价格是:%.2f' % new_price)  # 88.20


num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)  # 1
    num = 123
    print(num)  # 123


fun1()
print(num)  # 123

'''
闭包

1. 是函数式编程的一个重要的语法结构，是一种特殊的内嵌函数。
2. 如果在一个内部函数里对外层非全局作用域的变量进行引用，那么内部函数就被认为是闭包。
3. 通过闭包可以访问外层非全局作用域的变量，这个作用域称为 闭包作用域。
4.闭包的返回值通常是函数
5.如果要修改闭包作用域中的变量则需要 nonlocal 关键字
'''


def funX(x):
    def funY(y):
        return x * y
    return funY


i = funX(8)
print(type(i))  # <class 'function'>
print(i(5))  # 40


def make_counter(init):
    counter = [init]
    def inc(): counter[0] += 1
    def dec(): counter[0] -= 1
    def get(): return counter[0]
    def reset(): counter[0] = init
    return inc, dec, get, reset


inc, dec, get, reset = make_counter(0)
inc()
inc()
inc()
print(get())  # 3
dec()
print(get())  # 2
reset()
print(get())  # 0


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()
# 100
# 100

###########################################################
'''
Lambda表达式


在 Python 里有两类函数：
1. 第一类：用 def 关键词定义的正规函数
2. 第二类：用 lambda 关键词定义的匿名函数

lambda argument_list: expression

1. lambda - 定义匿名函数的关键词。
2. argument_list - 函数参数，它们可以是位置参数、默认参数、关键字参数，和正规函数里的参数类型一样。
3. : - 冒号，在函数参数和表达式中间要加个冒号。
4. expression - 只是一个表达式，输入函数参数，输出一些值。

注意：
1. expression 中没有 return 语句，因为 lambda 不需要它来返回，表达式本身结果就是返回值。
2. 匿名函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
'''


def sqr(x):
    return x ** 2


print(sqr)
# <function sqr at 0x000000BABD3A4400>
y = [sqr(x) for x in range(10)]
print(y)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
def lbd_sqr(x): return x ** 2


print(lbd_sqr)
# <function <lambda> at 0x000000BABB6AC1E0>
y = [lbd_sqr(x) for x in range(10)]
print(y)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
def sumary(arg1, arg2): return arg1 + arg2


print(sumary(10, 20))  # 30
func = lambda *args: sum(args)
print(func(1, 2, 3, 4, 5))  # 15

'''
函数式编程 

是指代码中每一块都是不可变的，都由纯函数的形式组成。这里的纯函数，是指函数本身相互独立、互不影
响，对于相同的输入，总会有相同的输出，没有任何副作用。

匿名函数 常常应用于函数式编程的高阶函数 (high-order function)中，主要有两种形式：
1. 参数是函数 (filter, map,reduce)
2. 返回值是函数 (closure)
'''

'''
e.g.，在 filter 和 map 函数中的应用：
1. filter(function, iterable) 过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，
可以使用 list() 来转换。
2.map(function, *iterables) 根据提供的函数对指定序列做映射。
3.reduce(function, *iterables) function取迭代器中的前两个数为参数，得出值后在和第三个值作为参数传入,依次计算
'''


# filter
def odd(x): return x % 2 == 1


templist = filter(odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(templist))  # [1, 3, 5, 7, 9]

# map
m1 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(m1))  # [1, 4, 9, 16, 25]
m2 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(m2))  # [3, 7, 11, 15, 19]

# reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4]))


def apply_to_list(fun, some_list):
    '''
    自己定义高阶函数
    '''
    return fun(some_list)


lst = [1, 2, 3, 4, 5]
print(apply_to_list(sum, lst))
# 15
print(apply_to_list(len, lst))
# 5
print(apply_to_list(lambda x: sum(x) / len(x), lst))
# 3.0
