'''文件操作
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None,
closefd=True)Open file and return a stream. Raise OSError upon failure.
a. file : 必需，文件路径（相对或者绝对路径）。
b. mode : 可选，文件打开模式
c. buffering : 设置缓冲
d. encoding : 一般使用utf8
e. errors : 报错级别
f. newline : 区分换行符

'r' 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
'w'打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑。即原有内容会被删除。
    如果该文件不存在，创建新文件。
'x' 写模式，新建一个文件，如果该文件已存在则会报错。
'a' 追加模式，打开一个文件用于追加。 如果该文件已存在，文件指针将会放在文件的结尾。
    也就是说，新的内容将会被写入到已有内容之后。 如果该文件不存在，创建新文件进行写入。
'b' 以二进制模式打开文件。一般用于非文本文件，如：图片。
't' 以文本模式打开（默认）。一般用于文本文件，如：txt。
'+' 可读写模式（可添加到其它模式中使用）

'''

'''
文件对象

fileObject.close() 用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError
错误。
fileObject.read([size]) 用于从文件读取指定的字符数，如果未给定或为负则读取所有。
fileObject.readline() 读取整行，包括 "\n" 字符。
fileObject.readlines() 用于读取所有行(直到结束符 EOF)并返回列表
fileObject.tell() 返回文件的当前位置，即文件指针当前位置。
fileObject.seek(offset[, whence]) 用于移动文件读取指针到指定位置。
    a. offset ：开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
    b. whence ：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始
    算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。

fileObject.write(str) 用于向文件中写入指定字符串，返回的是写入的字符长度
fileObject.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行
符。
'''

f = open('testfile.txt', 'r', encoding='UTF-8')
string = f.read(10)
print("读取的字符串: %s" % string)
line = f.readline()
print("读取的字符串: %s" % line)
lines = f.readlines()
print("读取的字符串: %s" % lines)
f.close()

# with语句
'''
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行它的清理方法
'''
try:
    with open('myfile.txt', 'r') as f:
        print(f.readline())
        for line in f:
            print(line)
except OSError as error:
    print('出错啦!%s' % str(error))
# 出错啦!not readable
