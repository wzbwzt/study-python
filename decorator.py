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
