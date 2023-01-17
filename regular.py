import re

"""
正则表达:
在以'r'为前缀的字符串文字中，反斜杠不以任何特殊的方式处理。所以r'\n'是一个包含“\”和“n”的双字符串，而“\n”是包含换行符的单字符串。

正则表达式修饰符—可选标志位:
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
修饰符被指定为一个可选的标志。多个标志可以通过按位 or(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

修饰符		描述信息
re.A		使\w，\W，\b，\B，\d，\D，\s和\S执行仅与ASCII匹配而不是完全的Unicode匹配。这只对Unicode模式有意义，对于字节模式将被忽略。
re.DEBUG	显示有关编译表达式的调试信息。
re.I		使匹配对大小写不敏感。
re.L		做本地化识别（locale-aware）匹配。
re.M		多行匹配，影响 ^ 和 $。
re.S		使 . 匹配包括换行在内的所有字符。
re.X		该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""


# re.match()
# 尝试从字符串的起始位置匹配，如果起始位置不能匹配，re.match()就返回None
s = "life is short, you need Python."
print(re.match(r'life', s))  # 从开始位置能成功匹配到
print(re.match(r'Life', s, re.I))  # 使用re.I标志位来指定忽略大小写
print(re.match(r'life', s).span())  # .span可以获取到具体匹配的起始位置
print(re.match(r'Python', s))  # 从开始位置不能成功匹配到

# re.group() re.groups()
# group(num=0)：匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()：返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
ret = re.match(r'(.*) is (.*)', s)
print("ret.group():", ret.group())
print("ret.group(1, 2):", ret.group(1, 2))
print("ret.group(1):", ret.group(1))
print("ret.group(2):", ret.group(2))
print("ret.groups():", ret.groups())
# 分组命名匹配：(?P<分组的名字>正则规则) 注意：是大写的P
ret = re.match(r'(?P<m1>.*) is (?P<m2>.*)', s)
print("ret.group():", ret.group())
print("ret.group('m1'):", ret.group('m1'))  # 支持使用组名访问匹配项
print("ret.group('m2'):", ret.group('m2'))
print("ret.group(1, 2):", ret.group(1, 2))
print("ret.group(1):", ret.group(1))
print("ret.group(2):", ret.group(2))
print("ret.groups():", ret.groups())

# re.search()
# 扫描整个字符串并返回第一个成功的匹配。注意与re.match()的区别
print(re.search(r'life', s))
print(re.search(r'life', s).span())
print(re.search(r'Python', s))
print(re.search(r'Python', s).span())
print(re.search(r'xxx', s))


# re.split()
# 用匹配到的对象将字符串分割成列表并返回。
s = "Abc123.aBc456.abC789"
ret1 = re.split(r'\.', s)  # 用.分割字符串s
ret2 = re.split(r'\.', s, 1)  # 用.分割字符串s，只分割一次
ret3 = re.split(r'[.\d]+', s)  # 用.和数字分s
print("用.分割字符串s:", ret1)
print("用.分割字符串s，只分割一次:", ret2)
print("用.和数字分s:", ret3)


# re.findall()
ret = re.findall(r'\d+', s)    # 找到所有的连续数字，并以列表形式返回
print("所有的数字：", ret)


# re.sub()
# 替换字符串中的匹配项。
s = "life is short, you need Python.  # 人生苦短，我用Python。"
s1 = re.sub(r'#.*$', "", s)  # 删除#及后面的内容（把#及后面的字符替换成空字符串）
print("去掉注释后：", s1)
# repl参数也可以是函数


def double(matched):
    num = int(matched.group("num"))  # 注意要转成int类型
    return str(num * 2)  # 将乘以2后的结果转成str类型


s = "1 + 2 = 3"
s1 = re.sub(r'(?P<num>\d+)', double, s)  # 分组命名匹配
print("re.sub替换后：", s1)

# re.compile()
'''
将正则表达式模式编译为正则表达式对象，可用于使用其match()和search()方法进行匹配
   re_obj = re.compile(pattern)
   ret = re_obj.match(string)
等价于:
    re.match(pattern,string)
'''
