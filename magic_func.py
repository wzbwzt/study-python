#魔法方法
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

#__init__(self[, ...])
'''
构造器，当一个实例被创建的时候调用的初始化方法
'''
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x + self.y) * 2
    def getArea(self):
        return self.x * self.y

rect = Rectangle(4, 5)
print(rect.getPeri()) # 18
print(rect.getArea()) # 20

#__new__(cls[, ...])
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
        return super().__new__(A, *args, **kwargs) # 改动了cls变为A
        
b = B(10)
    # 结果：
    # into B __new__
    # <class '__main__.B'>
    # into A __new__
    # <class '__main__.A'>


#__del__(self)
'''
析构器，当一个对象将要被系统回收之时调用的方法

Python 采用自动引用计数（ARC）方式来回收对象所占用的空间，当程序中有一个变量引用该 Python 对象时，Python 
会自动保证该对象引用计数为 1；当程序中有两个变量引用该 Python 对象时，Python 会自动保证该对象引用计数为 2，
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
    """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.name = new_name
        self.age = new_age
    def __str__(self):
    """返回一个对象的描述信息"""
        return "名字是:%s , 年龄是:%d" % (self.name, self.age)
    def __repr__(self):
    """返回一个对象的描述信息"""
    return "Cat:(%s,%d)" % (self.name, self.age)
    def eat(self):
        print("%s在吃鱼...." % self.name)
    def drink(self):
        print("%s在喝可乐..." % self.name)
    def introduce(self):
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))

# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom) # 名字是:汤姆 , 年龄是:30
print(str(tom)) # 名字是:汤姆 , 年龄是:30
print(repr(tom)) # Cat:(汤姆,30)
tom.eat() # 汤姆在吃鱼....
tom.introduce() # 名字是:汤姆, 年龄是:30