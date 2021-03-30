import os
import subprocess
'''
调用cmd后者shell命令

os.system 无法获取有返回的命令
os.popen 以字符串来获取字符输出
subprocess.Popen()
'''
#1.
cmd = 'ping baidu.com'
# res = os.popen(cmd)
# output_str = res.read()   # 获得输出字符串
# print(output_str)

#2.
# res = os.system(cmd)

#3.
output=subprocess.Popen(["ping","www.baidu.com"]).communicate()[0]
print(output)
if ("unreachable"in output):
    print("Offline")