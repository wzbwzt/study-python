# print函数介绍
'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

1. 将对象以字符串表示的方式格式化输出到流文件对象file里。其中所有非关键字参数都按 str() 方式进行转换为字符
串输出；
2. 关键字参数 sep 是实现分隔符，比如多个参数输出时想要输出中间的分隔字符；
3. 关键字参数 end 是输出结束时的字符，默认是换行符 \n ；
4. 关键字参数 file 是定义流输出的文件，可以是标准的系统输出 sys.stdout ，也可以重定义为别的文件；
5. 关键字参数 flush 是立即把内容输出到流文件，不作缓存。

'''

shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed without 'end'and 'sep'.")
for item in shoplist:
    print(item)  # 使用默认的值，每次打印自动换行
# This is printed without 'end'and 'sep'.
# apple
# mango
# carrot
# banana

shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed with 'end='&''.")
for item in shoplist:
    print(item, end='&')  # 指定末尾以&分割
print('hello world')

# This is printed with 'end='&''.
# apple&mango&carrot&banana&hello world
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed with 'sep='&''.")
for item in shoplist:
    print(item, 'another string', sep='&')  # 指定以&进行分割
# This is printed with 'sep='&''.
# apple&another string
# mango&another string
# carrot&another string
# banana&another string
