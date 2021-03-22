#元组
'''
「元组」定义语法为： (元素1, 元素2, ..., 元素n)
1. 小括号把所有元素绑在一起
2. 逗号将每个元素一一分开

Python 的元组与列表类似，不同之处在于tuple被创建后就不能对其进行修改，类似字符串

创建元组可以用小括号 ()，也可以什么都不用，为了可读性，建议还是用 ()
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
'''
t1 = (1, 10.31, 'python')
t2 = 1, 10.31, 'python'
print(t1, type(t1))
# (1, 10.31, 'python') <class 'tuple'>
print(t2, type(t2))
# (1, 10.31, 'python') <class 'tuple'>
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1[1]) # 2
print(tuple1[5:]) # (6, 7, 8)
print(tuple1[:5]) # (1, 2, 3, 4, 5)
tuple2 = tuple1[:]
print(tuple2) # (1, 2, 3, 4, 5, 6, 7, 8)

temp = (1,)
print(type(temp)) # <class 'tuple'>

#二维元祖
nested = (1, 10.31, 'python'), ('data', 11)
print(nested)
# ((1, 10.31, 'python'), ('data', 11))


week = ('Monday', 'Tuesday', 'Thursday', 'Friday')
week = week[:2] + ('Wednesday',) + week[2:]
print(week) # ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')


#元组有不可更改 (immutable) 的性质，因此不能直接给元组的元素赋值，但是只要元组中的元素可更改 (mutable)，那么我
#们可以直接更改其元素，注意这跟赋值其元素不同。
t1 = (1, 2, 3, [4, 5, 6])
print(t1) # (1, 2, 3, [4, 5, 6])
t1[3][0] = 9
print(t1) # (1, 2, 3, [9, 5, 6])

#元组相关的操作符
'''
1. 比较操作符
2. 逻辑操作符
3. 连接操作符 + 4. 重复操作符 * 5. 成员关系操作符 in 、 not in

元组拼接 (concatenate) 有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。

'''

#元组大小和内容都不可更改，因此只有 count 和 index 两种方法。
t = (1, 10.31, 'python')
#count('python') 是记录在元组 t 中该元素出现几次，显然是 1 次
print(t.count('python')) # 1
print(t.index(10.31)) # 1


#解压元组
'''
解压（unpack）一维元组（有几个元素左边括号定义几个变量）
'''
t = (1, 10.31, 'python')
(a, b, c) = t
print(a, b, c)
# 1 10.31 python
'''
解压二维元组（按照元组里的元组结构来定义变量）
'''
t = (1, 10.31, ('OK', 'python'))
(a, b, (c, d)) = t
print(a, b, c, d)
# 1 10.31 OK python

'''
如果你只想要元组其中几个元素，用通配符「*」，英文叫 wildcard，在计算机语言中代表一个或多个元素。下例
就是把多个元素丢给了 rest 变量。
'''
t = 1, 2, 3, 4, 5
a, b, *rest, c = t
print(a, b, c) # 1 2 5
print(rest) # [3, 4]

'''
如果你根本不在乎 rest 变量，那么就用通配符「*」加上下划线「_」。
'''
a, b, *_ = t
print(a, b) # 1 2