import time
import random

# 装饰器
# 总结一下就是：不修改源代码，不修改调用方式，同时还要加上新功能。


# 装饰index
def timer(func):  # 传一个func参数和下面func = index一样都是在my_index函数内部定义了一个局部变量
    def wrapper():  # 设置一个参数
        start_time = time.time()
        func()  # 在这个函数内部调用下func
        stop_time = time.time()
        print("耗时{}秒。".format(stop_time - start_time))
    return wrapper


@timer  # 相当于做了 index = timer(index) 操作
def index():
    time.sleep(random.randrange(1, 5))  # 随机sleep几秒
    print("欢迎访问首页。")


# 方式一
# index = timer(index)

# index()

# 方式二：推荐使用
# 在被装饰对象的正上方单独的一行写上@装饰器名即可，即：
index()

print("============================多装饰器===========================================")


def foo1(func):
    print("d1")

    def inner1():
        print("inner1")
        return "<i>{}</i>".format(func())

    return inner1


def foo2(func):
    print("d2")

    def inner2():
        print("inner2")
        return "<b>{}</b>".format(func())

    return inner2


@foo1
@foo2
def f1():
    return "Hello Andy"


print(f1())


print("========================== 带参数的装饰器 ========================================")


def d(a=None):  # 定义一个外层函数，给装饰器传参数--role
    def foo(func):  # foo是我们原来的装饰器函数，func是被装饰的函数
        def bar(*args, **kwargs):  # args和kwargs是被装饰器函数的参数
            # 根据装饰器的参数做一些逻辑判断
            if a:
                print("欢迎来到{}页面。".format(a))
            else:
                print("欢迎来到首页。")
            # 调用被装饰的函数，接收参数args和kwargs
            func(*args, **kwargs)
        return bar
    return foo


@d()  # 不给装饰器传参数，使用默认的'None'参数
def index(name):
    print("Hello {}.".format(name))


@d("电影")  # 给装饰器传一个'电影'参数
def movie(name):
    print("Hello {}.".format(name))


if __name__ == '__main__':
    index("Andy")
    movie("Andy")


print("================================== 类装饰器 ======================")


class D(object):
    def __init__(self, a=None):
        self.a = a
        self.mode = "装饰"

    def __call__(self, *args, **kwargs):
        if self.mode == "装饰":
            self.func = args[0]  # 默认第一个参数是被装饰的函数
            self.mode = "调用"
            return self
        # 当self.mode == "调用"时，执行下面的代码（也就是调用使用类装饰的函数时执行）
        if self.a:
            print("欢迎来到{}页面。".format(self.a))
        else:
            print("欢迎来到首页。")
        self.func(*args, **kwargs)


@D()
def index(name):
    print("Hello {}.".format(name))


@D("电影")
def movie(name):
    print("Hello {}.".format(name))


if __name__ == '__main__':
    index("Andy")
    movie("Andy")


print("================================== 装饰类 ======================")


# 定义一个类装饰器
class D(object):
    def __call__(self, cls):
        class Inner(cls):
            # 重写被装饰类的f方法
            def f(self):
                print("Hello Andy.")
        return Inner


@D()
class C(object):  # 被装饰的类
    # 有一个实例方法
    def f(self):
        print("Hello world.")


if __name__ == '__main__':
    c = C()
    c.f()
