# 魔法方法
'''
Python 的对象天生拥有一些神奇的方法，它们是面向对象的 Python 的一切...
它们是可以给你的类增加魔力的特殊方法...
如果你的对象实现了这些方法中的某一个，那么这个方法就会在特殊的情况下被 Python 所调用，而这一切都是自动发生
的

1.魔法方法总是被双下划线包围，例如 __init__ 。
2.魔法方法的第一个参数应为 cls （类方法） 或者 self （实例方法）。
    cls ：代表一个类的名称
    self ：代表一个实例对象的名称
'''

# __init__(self[, ...])
'''
构造器，当一个实例被创建的时候调用的初始化方法
'''




import datetime
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y


rect = Rectangle(4, 5)
print(rect.getPeri())  # 18
print(rect.getArea())  # 20

# __new__(cls[, ...])
'''
1. __new__ 是在一个对象实例化的时候所调用的第一个方法，在调用 __init__ 初始化前，先调用 __new__ 。
2. __new__ 至少要有一个参数 cls ，代表要实例化的类，此参数在实例化时由 Python 解释器自动提供，后面的参数直
接传递给 __init__ 。
3. __new__ 对当前类进行了实例化，并将实例返回，传给 __init__ 的 self 。但是，执行了 __new__ ，并不一定会
进入 __init__ ，只有 __new__ 返回了，当前类 cls 的实例，当前类的 __init__ 才会进入。
'''


class A(object):
    def __init__(self, value):
        print("into A __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into A __new__")
        print(cls)
        return object.__new__(cls)


class B(A):
    def __init__(self, value):
        print("into B __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into B __new__")
        print(cls)
        return super().__new__(cls, *args, **kwargs)


b = B(10)
# 结果：
# into B __new__
# <class '__main__.B'>
# into A __new__
# <class '__main__.B'>
# into B __init__

'''
1. 若 __new__ 没有正确返回当前类 cls 的实例，那 __init__ 是不会被调用的，即使是父类的实例也不行，将没
有 __init__ 被调用。
2. 可利用 __new__ 实现单例模式。
'''


class A(object):
    def __init__(self, value):
        print("into A __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into A __new__")
        print(cls)
        return object.__new__(cls)


class B(A):
    def __init__(self, value):
        print("into B __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into B __new__")
        print(cls)
        return super().__new__(A, *args, **kwargs)  # 改动了cls变为A


b = B(10)
# 结果：
# into B __new__
# <class '__main__.B'>
# into A __new__
# <class '__main__.A'>


# __del__(self)
'''
析构器，当一个对象将要被系统回收之时调用的方法

Python 采用自动引用计数（ARC）方式来回收对象所占用的空间，当程序中有一个变量引用该 Python 对象时，Python 
会自动保证该对象引用计数为 1;当程序中有两个变量引用该 Python 对象时，Python 会自动保证该对象引用计数为 2，
依此类推，如果一个对象的引用计数变成了 0，则说明程序中不再有变量引用该对象，表明程序不再需要该对象，因此
Python 就会回收该对象。
大部分时候，Python 的 ARC 都能准确、高效地回收系统中的每个对象。但如果系统中出现循环引用的情况，比如对象
a 持有一个实例变量引用对象 b，而对象 b 又持有一个实例变量引用对象 a，此时两个对象的引用计数都是 1，而实际上
程序已经不再有变量引用它们，系统应该回收它们，此时 Python 的垃圾回收器就可能没那么快，要等专门的循环垃圾
回收器（Cyclic Garbage Collector）来检测并回收这种引用循环。
'''


class C(object):
    def __init__(self):
        print('into C __init__')

    def __del__(self):
        print('into C __del__')


c1 = C()
# into C __init__
c2 = c1
c3 = c2
del c3
del c2
del c1
# into C __del__

'''
__str__(self) :
1. 当你打印一个对象的时候，触发 __str__
2. 当你使用 %s 格式化的时候，触发 __str__
3. str 强转数据类型的时候，触发 __str__
__repr__(self):
1. repr 是 str 的备胎
2. 有 __str__ 的时候执行 __str__ ,没有实现 __str__ 的时候，执行 __repr__
3. repr(obj) 内置函数对应的结果是 __repr__ 的返回值
4. 当你使用 %r 格式化的时候 触发 __repr__
'''


class Cat:
    """定义一个猫类"""

    def __init__(self, new_name, new_age):
        # 在创建完对象之后 会自动调用, 它完成对象的初始化的功能
        self.name = new_name
        self.age = new_age

    def __str__(self):
        # 返回一个对象的描述信息
        return "名字是:%s , 年龄是:%d" % (self.name, self.age)

    def __repr__(self):
        # 返回一个对象的描述信息
        return "Cat:(%s,%d)" % (self.name, self.age)

    def eat(self):
        print("%s在吃鱼...." % self.name)

    def drink(self):
        print("%s在喝可乐..." % self.name)

    def introduce(self):
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))


# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom)  # 名字是:汤姆 , 年龄是:30
print(str(tom))  # 名字是:汤姆 , 年龄是:30
print(repr(tom))  # Cat:(汤姆,30)
tom.eat()  # 汤姆在吃鱼....
tom.introduce()  # 名字是:汤姆, 年龄是:30

'''
__str__(self) 的返回结果可读性强。也就是说， __str__ 的意义是得到便于人们阅读的信息，就像下面的 '2019-10-
11' 一样。
__repr__(self) 的返回结果应更准确。怎么说， __repr__ 存在的目的在于调试，便于开发者使用。
'''

today = datetime.date.today()
print(str(today))  # 2019-10-11
print(repr(today))  # datetime.date(2019, 10, 11)
print('%s' % today)  # 2019-10-11
print('%r' % today)  # datetime.date(2019, 10, 11)

'''
算数运算符

 __add__(self, other) 定义加法的行为： +
 __sub__(self, other) 定义减法的行为： -
 __mul__(self, other) 定义乘法的行为： *
 __truediv__(self, other) 定义真除法的行为： /
 __floordiv__(self, other) 定义整数除法的行为： //
 __mod__(self, other) 定义取模算法的行为： %
 __divmod__(self, other) 定义当被 divmod() 调用时的行为
    divmod(a, b) 把除数和余数运算结果结合起来，返回一个包含商和余数的元组 (a // b, a % b) 。
        print(divmod(7, 2)) # (3, 1)
        print(divmod(8, 2)) # (4, 0)

__pow__(self, other[, module]) 定义当被 power() 调用或 ** 运算时的行为
__lshift__(self, other) 定义按位左移位的行为： <<
__rshift__(self, other) 定义按位右移位的行为： >>
__and__(self, other) 定义按位与操作的行为： &
__xor__(self, other) 定义按位异或操作的行为： ^
__or__(self, other) 定义按位或操作的行为： |
'''


class MyClass:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # 两个对象的长相加，宽不变.返回一个新的类
    def __add__(self, others):
        return MyClass(self.height + others.height, self.weight + others.weight)

    # 两个对象的宽相减，长不变.返回一个新的类
    def __sub__(self, others):
        return MyClass(self.height - others.height, self.weight - others.weight)

    # 说一下自己的参数
    def intro(self):
        print("高为", self.height, " 重为", self.weight)


def main():
    a = MyClass(height=10, weight=5)
    a.intro()
    b = MyClass(height=20, weight=10)
    b.intro()
    c = b - a
    c.intro()
    d = a + b
    d.intro()


if __name__ == '__main__':
    main()
# 高为 10 重为 5
# 高为 20 重为 10
# 高为 10 重为 5
# 高为 30 重为 15

'''
反算术运算符

1. __radd__(self, other) 定义加法的行为： +
2. __rsub__(self, other) 定义减法的行为： -
3. __rmul__(self, other) 定义乘法的行为： *
4. __rtruediv__(self, other) 定义真除法的行为： /
5. __rfloordiv__(self, other) 定义整数除法的行为： //
6. __rmod__(self, other) 定义取模算法的行为： %
7. __rdivmod__(self, other) 定义当被 divmod() 调用时的行为
8. __rpow__(self, other[, module]) 定义当被 power() 调用或 ** 运算时的行为
9. __rlshift__(self, other) 定义按位左移位的行为： <<
10. __rrshift__(self, other) 定义按位右移位的行为： >>
11. __rand__(self, other) 定义按位与操作的行为： &
12. __rxor__(self, other) 定义按位异或操作的行为： ^
13. __ror__(self, other) 定义按位或操作的行为： |
'''

'''
a + b
这里加数是 a ，被加数是 b ，因此是 a 主动，反运算就是如果 a 对象的 __add__() 方法没有实现或者不支持相应的操
作，那么 Python 就会调用 b 的 __radd__() 方法。
'''


class Nint(int):
    def __radd__(self, other):
        return int.__sub__(other, self)  # 注意 self 在后面


a = Nint(5)
b = Nint(3)
print(a + b)  # 8
print(1 + b)  # -2


'''
增量赋值运算符
1. __iadd__(self, other) 定义赋值加法的行为： +=
2. __isub__(self, other) 定义赋值减法的行为： -=
3. __imul__(self, other) 定义赋值乘法的行为： *=
4. __itruediv__(self, other) 定义赋值真除法的行为： /=
5. __ifloordiv__(self, other) 定义赋值整数除法的行为： //=
6. __imod__(self, other) 定义赋值取模算法的行为： %=
7. __ipow__(self, other[, modulo]) 定义赋值幂运算的行为： **=
8. __ilshift__(self, other) 定义赋值按位左移位的行为： <<=
9. __irshift__(self, other) 定义赋值按位右移位的行为： >>=
10. __iand__(self, other) 定义赋值按位与操作的行为： &=
11. __ixor__(self, other) 定义赋值按位异或操作的行为： ^=
12. __ior__(self, other) 定义赋值按位或操作的行为： |=
'''

'''
一元运算符

1. __neg__(self) 定义正号的行为： +x
2. __pos__(self) 定义负号的行为： -x
3. __abs__(self) 定义当被 abs() 调用时的行为
4. __invert__(self) 定义按位求反的行为： ~x
'''


'''
属性访问

__getattr__ ， __getattribute__ ， __setattr__ 和 __delattr__
__getattr__(self, name) : 定义当用户试图获取一个不存在的属性时的行为。
__getattribute__(self, name) ：定义当该类的属性被访问时的行为（先调用该方法，查看是否存在该属性，若不存
在，接着去调用 __getattr__ ）。
__setattr__(self, name, value) ：定义当一个属性被设置时的行为。
__delattr__(self, name) ：定义当一个属性被删除时的行为。

'''


class C:
    def __getattribute__(self, item):
        print('__getattribute__')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print('__getattr__')

    def __setattr__(self, key, value):
        print('__setattr__')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print('__delattr__')
        super().__delattr__(item)


c = C()
c.x

# __getattribute__
# __getattr__
c.x = 1
# __setattr__
del c.x
# __delattr__

'''
描述符

描述符就是将某种特殊类型的类的实例指派给另一个类的属性。
1. __get__(self, instance, owner) 用于访问属性，它返回属性的值。
2. __set__(self, instance, value) 将在属性分配操作中调用，不返回任何内容。
3. __del__(self, instance) 控制删除操作，不返回任何内容。
'''


class MyDecriptor:
    def __get__(self, instance, owner):
        print('__get__', self, instance, owner)

    def __set__(self, instance, value):
        print('__set__', self, instance, value)

    def __delete__(self, instance):
        print('__delete__', self, instance)


class Test:
    x = MyDecriptor()


t = Test()
t.x
# __get__ <__main__.MyDecriptor object at 0x000000CEAAEB6B00> <__main__.Test object at
# 0x000000CEABDC0898 > <class '__main__.Test' >

t.x = 'x-man'
# __set__ <__main__.MyDecriptor object at 0x00000023687C6B00> <__main__.Test object at
#0x00000023696B0940 > x-man
del t.x
# __delete__ <__main__.MyDecriptor object at 0x000000EC9B160A90> <__main__.Test object at
# 0x000000EC9B160B38 >


'''
定制序列

协议（Protocols）与其它编程语言中的接口很相似，它规定你哪些方法必须要定义。然而，在 Python 中的协议就显得不那
么正式。事实上，在 Python 中，协议更像是一种指南。

容器类型的协议
1. 如果说你希望定制的容器是不可变的话，你只需要定义 __len__() 和 __getitem__() 方法。
2. 如果你希望定制的容器是可变的话，除了 __len__() 和 __getitem__() 方法，你还需要定义 __setitem__()
和 __delitem__() 两个方法。

 __len__(self) 定义当被 len() 调用时的行为（返回容器中元素的个数）。
 __getitem__(self, key) 定义获取容器中元素的行为，相当于 self[key] 。
 __setitem__(self, key, value) 定义设置容器中指定元素的行为，相当于 self[key] = value 。
 __delitem__(self, key) 定义删除容器中指定元素的行为，相当于 del self[key] 。
'''


class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]
        for i in range(0, len(self.values)):
            if i >= key:
                self.count[i] = self.count[i + 1]
                self.count.pop(len(self.values))


c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
print(c1[1])  # 3
print(c2[2])  # 6
c2[2] = 12
print(c1[1] + c2[2])  # 15
print(c1.count)
# {0: 0, 1: 2, 2: 0, 3: 0, 4: 0}
print(c2.count)
# {0: 0, 1: 0, 2: 2, 3: 0, 4: 0}
# del c1[1]
print(c1.count)
# {0: 0, 1: 0, 2: 0, 3: 0}
