import pickle
'''
序列化与反序列化

pickle.dump(obj, file, [,protocol]) 将 obj 对象序列化存入已经打开的 file 中。
1. obj ：想要序列化的 obj 对象。
2. file :文件名称。
3. protocol ：序列化使用的协议。如果该项省略，则默认为0。如果为负值或 HIGHEST_PROTOCOL ，则使用最高的协
议版本
'''

'''
pickle.load(file) 将 file 中的对象序列化读出。
1. file ：文件名称。
'''

dataList = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
dataDic = {0: [1, 2, 3, 4],
           1: ('a', 'b'),
           2: {'c': 'yes', 'd': 'no'}}
# 使用dump()将数据序列化到文件中
fw = open(r'.\dataFile.pkl', 'wb')
# Pickle the list using the highest protocol available.
pickle.dump(dataList, fw, -1)
# Pickle dictionary using protocol 0.
pickle.dump(dataDic, fw)
fw.close()
# 使用load()将数据从文件中序列化读出
fr = open('dataFile.pkl', 'rb')
data1 = pickle.load(fr)
print(data1)
data2 = pickle.load(fr)
print(data2)
fr.close()
# [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
# {0: [1, 2, 3, 4], 1: ('a', 'b'), 2: {'c': 'yes', 'd': 'no'}}
