#集合
'''
set 与 dict 类似，也是一组 key 的集合，但不存储 value 。由于 key 不能重复，所以，在 set 中，没有重复
的 key
集合的两个特点：无序 (unordered) 和唯一 (unique)。

注意， key 为不可变类型，即可哈希的值。
'''
num = {}
print(type(num)) # <class 'dict'>
num = {1, 2, 3, 4}
print(type(num)) # <class 'set'>

#集合的创建
'''
1. 先创建对象再加入元素。
2. 在创建空集合的时候只能使用 s = set() ，因为 s = {} 创建的是空字典。
'''
basket = set()
basket.add('apple')
basket.add('banana')
print(basket) # {'banana', 'apple'}

'''
1. 直接把一堆元素用花括号括起来 {元素1, 元素2, ..., 元素n} 。
2. 重复元素在 set 中会被自动被过滤。
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'banana', 'apple', 'pear', 'orange'}

'''
使用 set(value) 工厂函数，把列表或元组转换成集合。
'''
a = set('abracadabra')
print(a) 
# {'r', 'b', 'd', 'c', 'a'}
b = set(("Google", "Lsgogroup", "Taobao", "Taobao"))
print(b) 
# {'Taobao', 'Lsgogroup', 'Google'}
c = set(["Google", "Lsgogroup", "Taobao", "Google"])
print(c) 
# {'Taobao', 'Lsgogroup', 'Google'}

#访问集合中的值
'''
使用 len() 內建函数得到集合的大小
'''
thisset = set(['Google', 'Baidu', 'Taobao'])
print(len(thisset)) # 3

'''
可以使用 for 把集合中的数据一个个读取出来。
'''
thisset = set(['Google', 'Baidu', 'Taobao'])
for item in thisset:
	print(item)
# Baidu
# Google
# Taobao
'''
通过 in 或 not in 判断一个元素是否在集合中已经存在
'''
thisset = set(['Google', 'Baidu', 'Taobao'])
print('Taobao' in thisset) # True
print('Facebook' not in thisset) # True

#集合的内置方法
'''
set.add(elmnt) 用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
'''
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) 
# {'orange', 'cherry', 'banana', 'apple'}
fruits.add("apple")
print(fruits) 
# {'orange', 'cherry', 'banana', 'apple'}

'''
set.update(set) 用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，
则该元素只会出现一次，重复的会忽略。
'''
x = {"apple", "banana", "cherry"}
y = {"google", "baidu", "apple"}
x.update(y)
print(x)
# {'cherry', 'banana', 'apple', 'google', 'baidu'}
y.update(["lsgo", "dreamtech"])
print(y)
# {'lsgo', 'baidu', 'dreamtech', 'apple', 'google'}

'''
set.remove(item) 用于移除集合中的指定元素。如果元素不存在，则会发生错误。
set.discard(value) 用于移除指定的集合元素。 remove() 方法在移除一个不存在的元素时会发生错误，而
discard() 方法不会。
'''
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # {'apple', 'cherry'}

'''
set.pop() 用于随机移除一个元素
'''
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(fruits) # {'cherry', 'apple'}
print(x) # banana

'''
1.set.intersection(set1, set2 ...) 返回两个集合的交集。
2. set1 & set2 返回两个集合的交集。
3. set.intersection_update(set1, set2 ...) 交集，在原始的集合上移除不重叠的元素。
'''
a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
c = a.intersection(b)
print(c) # {'a', 'c'}
print(a & b) # {'c', 'a'}
print(a) # {'a', 'r', 'c', 'b', 'd'}
a.intersection_update(b)
print(a) # {'a', 'c'}

'''
1.set.union(set1, set2...) 返回两个集合的并集。
2. set1 | set2 返回两个集合的并集。
'''
a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
print(a | b) # {'l', 'd', 'm', 'b', 'a', 'r', 'z', 'c'}
c = a.union(b)
print(c) # {'c', 'a', 'd', 'm', 'r', 'b', 'z', 'l'}

'''
1.set.difference(set) 返回集合的差集。
2. set1 - set2 返回集合的差集。
3. set.difference_update(set) 集合的差集，直接在原来的集合中移除元素，没有返回值
'''
a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
c = a.difference(b)
print(c) # {'b', 'd', 'r'}
print(a - b) # {'d', 'b', 'r'}
print(a) # {'r', 'd', 'c', 'a', 'b'}
a.difference_update(b)
print(a) # {'d', 'r', 'b'}

'''
1.set.symmetric_difference(set) 返回集合的异或。
2. set1 ^ set2 返回集合的异或。
3. set.symmetric_difference_update(set) 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定
集合中不同的元素插入到当前集合中
'''
a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
c = a.symmetric_difference(b)
print(c) # {'m', 'r', 'l', 'b', 'z', 'd'}
print(a ^ b) # {'m', 'r', 'l', 'b', 'z', 'd'}
print(a) # {'r', 'd', 'c', 'a', 'b'}
a.symmetric_difference_update(b)
print(a) # {'r', 'b', 'm', 'l', 'z', 'd'}

'''
1.set.issubset(set) 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
2. set1 <= set2 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
'''
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z) # True
print(x <= y) # True
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z) # False
print(x <= y) # False

'''
1. set.issuperset(set) 用于判断集合是不是包含其他集合，如果是则返回 True，否则返回 False。
2. set1 >= set2 判断集合是不是包含其他集合，如果是则返回 True，否则返回 False。
'''
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) # True
print(x >= y) # True
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) # False
print(x >= y) # False

'''
set.isdisjoint(set) 用于判断两个集合是不是不相交，如果是返回 True，否则返回 False。
'''
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.isdisjoint(y)
print(z) # False
x = {"f", "e", "d", "m", "g"}
y = {"a", "b", "c"}
z = x.isdisjoint(y)
print(z) # True

'''
集合的转换
'''
se = set(range(4))
li = list(se)
tu = tuple(se)
print(se, type(se)) # {0, 1, 2, 3} <class 'set'>
print(li, type(li)) # [0, 1, 2, 3] <class 'list'>
print(tu, type(tu)) # (0, 1, 2, 3) <class 'tuple'>

'''
不可变集合
Python 提供了不能改变元素的集合的实现版本，即不能增加或删除元素，类型名叫 frozenset 。需要注意的
是 frozenset 仍然可以进行集合操作，只是不能用带有 update 的方法。
'''

a = frozenset(range(10)) # 生成一个新的不可变集合
print(a) 
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
b = frozenset('lsgogroup')
print(b) 
# frozenset({'g', 's', 'p', 'r', 'u', 'o', 'l'})

'''
zip(iter1 [,iter2 [...]])

a. 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样
做的好处是节约了不少的内存。
b. 我们可以使用 list() 转换来输出列表。
c. 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为
列表。
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)
print(zipped) # <zip object at 0x000000C5D89EDD88>
print(list(zipped)) # [(1, 4), (2, 5), (3, 6)]
zipped = zip(a, c)
print(list(zipped)) # [(1, 4), (2, 5), (3, 6)]
a1, a2 = zip(*zip(a, b))
print(list(a1)) # [1, 2, 3]
print(list(a2)) # [4, 5, 6]