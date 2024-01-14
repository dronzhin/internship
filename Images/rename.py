import os
import shutil

path = '2022/'

paths = []
for i in os.listdir(path):
    name = path + i
    paths.append(name)

for i in os.listdir(path):
    name = path + i
    if name[-3:] == '-1p' or name[-3:] == '-1р' or name[-3:] == '_1p' or name[-3:] == '_1р':
        if name[:-3] not in paths:
            os.rename(name, name[:-3])

paths = []
for i in os.listdir(path):
    name = path + i
    paths.append(name)
for i in os.listdir(path):
    name = path + i
    if name[:-3] in paths:
        list_file = os.listdir(name)
        for file in list_file:
            our_file = os.path.join(name, file)
            shutil.move(our_file, name[:-3])
        print(f'Файлы из папки {name} перемещены')
        shutil.rmtree(name)