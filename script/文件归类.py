import os
import shutil
path = "./"
files = os.listdir(path)
print(files)

for f in files:
    print(f)
    floder_name = "./"+f.split(".")[-1]
    print(floder_name)
    if not os.path.exists(floder_name):
        os.makedirs(floder_name)
    shutil.move(f, floder_name)
