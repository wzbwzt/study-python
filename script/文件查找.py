import os

'''
文件查找
'''
Path = input("输入路径：")
File = input("输入文件名：")


def showFilePath(path):
    try:
        if File in path:
            print("查找路径是："+path)
        if os.path.isdir(path):
            for i in os.listdir(path):
                if File in i:
                    print("查找路径是："+os.path.join(path, i))
                if os.path.isdir(os.path.join(path, i)):
                    showFilePath(os.path.join(path, i))
    except (BaseException, FileNotFoundError, NotImplementedError)as error:
        print("err:"+str(error))


showFilePath(Path)
