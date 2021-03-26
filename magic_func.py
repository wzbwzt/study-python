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