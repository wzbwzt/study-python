# 字符串
'''
1. Python 中字符串被定义为引号之间的字符集合。
2. Python 支持使用成对的 单引号 或 双引号。
'''
'''
常用转义字符
\\ 反斜杠符号
\' 单引号
\" 双引号
\n 换行
\t 横向制表符(TAB)
\r 回车
'''

'''
原始字符串只需要在字符串前边加一个英文字母 r 即可。
'''
print(r'C:\Program Files\Intel\Wifi\Help')
# C:\Program Files\Intel\Wifi\Help

'''
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
'''
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)
'''
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( )。
也可以使用换行符 [ 
 ]。
'''

# 字符串的切片与拼接
'''
1. 类似于元组具有不可修改性
2. 从 0 开始 (和 C 一样)
3. 切片通常写成 start:end 这种形式，包括「 start 索引」对应的元素，不包括「 end 索引」对应的元素。
4. 索引值可正可负，正索引从 0 开始，从左往右；负索引从 -1 开始，从右往左。使用负数索引时，会从最后一个元素
开始计数。最后一个元素的位置编号是 -1。
'''

str1 = 'I Love LsgoGroup'
print(str1[:6])  # I Love
print(str1[5])  # e
print(str1[:6] + " 插入的字符串 " + str1[6:])
# I Love 插入的字符串 LsgoGroup
s = 'Python'
print(s)  # Python
print(s[2:4])  # th
print(s[-5:-2])  # yth
print(s[2])  # t
print(s[-1])  # n

# 字符串的常用内置方法
'''
capitalize() 将字符串的第一个字符转换为大写
lower() 转换字符串中所有大写字符为小写。
upper() 转换字符串中的小写字母为大写。
swapcase() 将字符串中大写转换为小写，小写转换为大写。
'''
str2 = 'xiaoxie'
print(str2.capitalize())  # Xiaoxie


'''
count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定
范围内 str 出现的次数。

endswith(suffix, beg=0, end=len(string)) 检查字符串是否以指定子字符串 suffix 结束，如果是，返回
True,否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查。
startswith(substr, beg=0,end=len(string)) 检查字符串是否以指定子字符串 substr 开头，如果是，返回
True，否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查。

find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是
否包含在指定范围内，如果包含，返回开始的索引值，否则返回 -1。
rfind(str, beg=0,end=len(string)) 类似于 find() 函数，不过是从右边开始查找。

isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False。
'''
str2 = "DAXIExiaoxie"
print(str2.count('xi'))  # 2

'''
ljust(width[, fillchar]) 返回一个原字符串左对齐，并使用 fillchar （默认空格）填充至长度 width 的新字
符串。
rjust(width[, fillchar]) 返回一个原字符串右对齐，并使用 fillchar （默认空格）填充至长度 width 的新字
符串。
'''
str4 = '1101'
print(str4.ljust(8, '0'))  # 11010000
print(str4.rjust(8, '0'))  # 00001101

'''
lstrip([chars]) 截掉字符串左边的空格或指定字符。
rstrip([chars]) 删除字符串末尾的空格或指定字符。
strip([chars]) 在字符串上执行 lstrip() 和 rstrip() 。
'''
str5 = ' I Love LsgoGroup '
print(str5.lstrip())  # 'I Love LsgoGroup '
print(str5.lstrip().strip('I'))  # ' Love LsgoGroup '
print(str5.rstrip())  # ' I Love LsgoGroup'
print(str5.strip())  # 'I Love LsgoGroup'
print(str5.strip().strip('p'))  # 'I Love LsgoGrou'

'''
partition(sub) 找到子字符串sub，把字符串分为一个三元组 (pre_sub,sub,fol_sub) ，如果字符串中不包含
sub则返回 ('原字符串','','') 。
rpartition(sub) 类似于 partition() 方法，不过是从右边开始查找。
'''
str5 = ' I Love LsgoGroup '
print(str5.strip().partition('o'))  # ('I L', 'o', 've LsgoGroup')
print(str5.strip().partition('m'))  # ('I Love LsgoGroup', '', '')
print(str5.strip().rpartition('o'))  # ('I Love LsgoGr', 'o', 'up')

'''
replace(old, new [, max]) 把 将字符串中的 old 替换成 new ，如果 max 指定，则替换不超过 max 
'''
str5 = ' I Love LsgoGroup '
print(str5.strip().replace('I', 'We'))  # We Love LsgoGroup

'''
split(str="", num) 不带参数默认是以空格为分隔符切片字符串，如果 num 参数有设置，则仅分隔 num 个子字符
串，返回切片后的子字符串拼接的列表。
'''
str5 = ' I Love LsgoGroup '
print(str5.strip().split())  # ['I', 'Love', 'LsgoGroup']
print(str5.strip().split('o'))  # ['I L', 've Lsg', 'Gr', 'up']

u = "www.baidu.com.cn"
# 使用默认分隔符
print(u.split())  # ['www.baidu.com.cn']
# 以"."为分隔符
print((u.split('.')))  # ['www', 'baidu', 'com', 'cn']
# 分割0次
print((u.split(".", 0)))  # ['www.baidu.com.cn']
# 分割一次
print((u.split(".", 1)))  # ['www', 'baidu.com.cn']
# 分割两次
print(u.split(".", 2))  # ['www', 'baidu', 'com.cn']
# 分割两次，并取序列为1的项
print((u.split(".", 2)[1]))  # baidu
# 分割两次，并把分割后的三个部分保存到三个变量
u1, u2, u3 = u.split(".", 2)
print(u1)  # www
print(u2)  # baidu
print(u3)  # com.cn

'''
splitlines([keepends]) 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为
False，不包含换行符，如果为 True，则保留换行符。

'''
str6 = 'I \n Love \n LsgoGroup'
print(str6.splitlines())  # ['I ', ' Love ', ' LsgoGroup']
print(str6.splitlines(True))  # ['I \n', ' Love \n', ' LsgoGroup']

'''
maketrans(intab, outtab) 创建字符映射的转换表，第一个参数是字符串，表示需要转换的字符，第二个参数也
是字符串表示转换的目标。
translate(table, deletechars="") 根据参数 table 给出的表，转换字符串的字符，要过滤掉的字符放
到 deletechars 参数中

'''
str = 'this is string example....wow!!!'
intab = 'aeiou'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
print(trantab)  # {97: 49, 111: 52, 117: 53, 101: 50, 105: 51}
print(str.translate(trantab))  # th3s 3s str3ng 2x1mpl2....w4w!!!

# 字符串格式化
'''
format格式话子串
'''
str = "{0} Love {1}".format('I', 'Lsgogroup')  # 位置参数
print(str)  # I Love Lsgogroup
str = "{a} Love {b}".format(a='I', b='Lsgogroup')  # 关键字参数
print(str)  # I Love Lsgogroup
str = "{0} Love {b}".format('I', b='Lsgogroup')  # 位置参数要在关键字参数之前
print(str)  # I Love Lsgogroup
str = '{0:.2f}{1}'.format(27.658, 'GB')  # 保留小数点后两位
print(str)  # 27.66GB

'''
字符串格式化符号

%c 格式化字符及其ASCII码
%s 格式化字符串，用str()方法处理对象
%r 格式化字符串，用rper()方法处理对象
%d 格式化整数
%o 格式化无符号八进制数
%x 格式化无符号十六进制数
%X 格式化无符号十六进制数（大写）
%f 格式化浮点数字，可指定小数点后的精度
%e 用科学计数法格式化浮点数
%E 作用同%e，用科学计数法格式化浮点数
%g 根据值的大小决定使用%f或%e
%G 作用同%g，根据值的大小决定使用%f或%E
'''
print('%c' % 97)  # a
print('%c %c %c' % (97, 98, 99))  # a b c
print('%d + %d = %d' % (4, 5, 9))  # 4 + 5 = 9
print("我叫 %s 今年 %d 岁!" % ('小明', 10))  # 我叫 小明 今年 10 岁!
print('%o' % 10)  # 12
print('%x' % 10)  # a
print('%X' % 10)  # A
print('%f' % 27.658)  # 27.658000
print('%e' % 27.658)  # 2.765800e+01
print('%E' % 27.658)  # 2.765800E+01
print('%g' % 27.658)  # 27.658
text = "I am %d years old." % 22
print("I said: %s." % text)  # I said: I am 22 years old..
print("I said: %r." % text)  # I said: 'I am 22 years old.'

# 格式化操作符辅助指令
'''
m.n m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话) - 用做左对齐
+ 在正数前面显示加号( + )
# 在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0 显示的数字前面填充'0'而不是默认的空格
'''
print('%5.1f' % 27.658)  # ' 27.7'
print('%.2e' % 27.658)  # 2.77e+01
print('%10d' % 10)  # ' 10'
print('%-10d' % 10)  # '10 '
print('%+d' % 10)  # +10
print('%#o' % 10)  # 0o12
print('%#x' % 108)  # 0x6c
print('%010d' % 5)  # 0000000005
