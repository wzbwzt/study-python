'''
容器 -> 数据的封装
函数 -> 语句的封装
类 -> 方法和属性的封装
模块 -> 程序文件
'''
'''
命名空间
Local Namespaces:本地命名空间
Global Namesspaces:全局命名空间
Built-in Namesspaces:内置命令空间

程序在查询上述三种命名空间的时候，就按照从里到外的顺序，即：Local Namespaces --> Global Namesspaces --> Built-in 
Namesspaces。
'''

'''
导入模板的方式
'''


# 方式1:import 模块名
'''
import TemperatureConversion
print('32摄氏度 = %.2f华氏度' % TemperatureConversion.c2f(32))
print('99华氏度 = %.2f摄氏度' % TemperatureConversion.f2c(99))
# 32摄氏度 = 89.60华氏度
# 99华氏度 = 37.22摄氏度
'''

# 方式2:from 模块名 import 函数名
'''
from TemperatureConversion import c2f, f2c
print('32摄氏度 = %.2f华氏度' % c2f(32))
print('99华氏度 = %.2f摄氏度' % f2c(99))
# 32摄氏度 = 89.60华氏度
# 99华氏度 = 37.22摄氏度

#不推荐
from TemperatureConversion import *
print('32摄氏度 = %.2f华氏度' % c2f(32))
print('99华氏度 = %.2f摄氏度' % f2c(99))
# 32摄氏度 = 89.60华氏度
# 99华氏度 = 37.22摄氏度
'''

# 方式3：import 模块名 as 新名字
'''
import TemperatureConversion as tc
print('32摄氏度 = %.2f华氏度' % tc.c2f(32))
print('99华氏度 = %.2f摄氏度' % tc.f2c(99))
# 32摄氏度 = 89.60华氏度
# 99华氏度 = 37.22摄氏度
'''

# if __name__ == '__main__'
'''
#const.py
PI = 3.14


def main():
    print("PI:", PI)


main()
# PI: 3.14
'''
'''
from const import PI
def calc_round_area(radius):
 return PI * (radius ** 2)
def main():
 print("round area: ", calc_round_area(2))

main()
#PI: 3.14 #PI 模块中的main也被运行了；其实PI中的main并不需要被运行；这时候需要将其区别开来
#round area: 12.56
'''
# 将const.py文件中的main（）做修改
'''
if __name__ == "__main__":
 main()

__name__ ：是内置变量，可用于表示当前模块的名字;

'''


'''
搜索路径

搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在 sys 模块中的 path 变
量中
'''
import sys
print(sys.path)
