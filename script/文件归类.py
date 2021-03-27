import os
import shutil
'''
文件递归归档
'''
path = input("输入归档文件路径:")

def arrangeFile(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        for f in files:
            if os.path.isdir(os.path.join(path,f)):
                arrangeFile(os.path.join(path,f))
            else:
                floder_name ="./"+f.split(".")[-1]
                if not os.path.exists(floder_name):
                    os.makedirs(floder_name)
                shutil.move(os.path.join(path,f), floder_name)
        

arrangeFile(path)

