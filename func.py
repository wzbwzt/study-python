
#函数
'''
1. 函数以 def 关键词开头，后接函数名和圆括号()。
2. 函数执行的代码以冒号起始，并且缩进。
3. return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None 。

def functionname(parameters):
 "函数_文档字符串"
 function_suite
 return [expression]
'''

def add(a, b):
    print(a + b)
add(1, 2) # 3
add([1, 2, 3], [4, 5, 6]) # [1, 2, 3, 4, 5, 6]