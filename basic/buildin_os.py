'''
我们所知道常用的操作系统就有：Windows，Mac OS，Linu，Unix等，这些操作系统底层对于文件系统的访问工作原理是
不一样的，因此你可能就要针对不同的系统来考虑使用哪些文件系统模块……，这样的做法是非常不友好且麻烦的，因为
这样就意味着当你的程序运行环境一改变，你就要相应的去修改大量的代码来应对。
有了OS（Operation System）模块，我们不需要关心什么操作系统下使用什么模块，OS模块会帮你选择正确的模块并调
用
os.getcwd() 用于返回当前工作目录。
os.chdir(path) 用于改变当前工作目录到指定的路径 listdir (path='.') 返回 path 指定的文件夹包含的文件或文件夹的名字的列表。
os.mkdir(path) 创建单层目录，如果该目录已存在抛出异常
os.makedirs(path) 用于递归创建多层目录，如果该目录已存在抛出异常。
os.remove(path) 用于删除指定路径的文件。如果指定的路径是一个目录，将抛出 OSError 。
os.rmdir(path) 用于删除单层目录。仅当这文件夹是空的才可以, 否则, 抛出 OSError 。
os.removedirs(path) 递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常。
os.rename(src, dst) 方法用于命名文件或目录，从 src 到 dst ，如果 dst 是一个存在的目录, 将抛出 OSError
os.system(command) 运行系统的shell命令（将字符串转化成命令）
os.curdir 指代当前目录（ . ）
os.pardir 指代上一级目录（ .. ）
os.sep 输出操作系统特定的路径分隔符（win下为 \\ ，Linux下为 / ）
os.linesep 当前平台使用的行终止符（win下为 \r\n ，Linux下为 \n ）
os.name 指代当前使用的操作系统（包括：'mac'，'nt'）
os.path.basename(path) 去掉目录路径，单独返回文件名
os.path.dirname(path) 去掉文件名，单独返回目录路径
os.path.join(path1[, path2[, ...]]) 将 path1 ， path2 各部分组合成一个路径名
os.path.split(path) 分割文件名与路径，返回 (f_path,f_name) 元组。如果完全使用目录，它会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在。
os.path.splitext(path) 分离文件名与扩展名，返回 (f_path,f_name) 元组。
os.path.getsize(file) 返回指定文件大小，单位是字节。
os.path.getatime(file) 返回指定文件最近的访问时间
os.path.getctime(file) 返回指定文件的创建时间
os.path.getmtime(file) 返回指定文件的最新的修改时间 浮点型秒数，可用time模块的 gmtime() 或 localtime() 函数换算
os.path.exists(path) 判断指定路径（目录或文件）是否存在
os.path.isabs(path) 判断指定路径是否为绝对路径
os.path.isdir(path) 判断指定路径是否存在且是一个目录
os.path.isfile(path) 判断指定路径是否存在且是一个文件
os.path.islink(path) 判断指定路径是否存在且是一个符号链接
os.path.ismount(path) 判断指定路径是否存在且是一个悬挂点
os.path.samefile(path1,path2) 判断path1和path2两个路径是否指向同一个文件
os.stat('path/filename')  获取文件/目录信息
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
os.environ  获取系统环境变量
os.path.abspath(path)  返回path规范化的绝对路径
'''

import os
path = 'D:\\www\\python_study'
print("当前工作目录 : %s" % os.getcwd())

os.chdir(path)
print("目录修改成功 : %s" % os.getcwd())
# 目录修改成功 : C:\
print(os.listdir(path))

if os.path.isdir(r'.\b') is False:
    os.mkdir(r'.\B')
    os.mkdir(r'.\B\A')
os.mkdir(r'.\C\A')  # FileNotFoundError

print(os.curdir)  # .
print(os.pardir)  # ..
print(os.sep)  # \
print(os.linesep)
print(os.name)  # nt
