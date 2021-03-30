import time
from ctypes import cdll, c_char_p
# def fibonacci(num):
#     if num<=0:
#         return 0
#     if num==1 or num==2:
#         return 1
#     return fibonacci(num-1)+fibonacci(num-2)


# start=time.time()
# print(fibonacci(30))
# end=time.time()
# print(f"{end - start}s.")

# 832040
# 0.21982765197753906s

start = time.time()

# 加载动态链接库
lib = cdll.LoadLibrary('./main.so')

# 配置输出参数变量类型
lib.Count_time.restype = c_char_p

# 调用方法
rest = lib.Count_time()

end = time.time()

print(f"Go 内部执行时间：{rest}")
print(f"Python 整体执行时间: {end - start}s")
