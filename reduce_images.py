import os
from PIL import Image

path_old = 'Images'
path_new = 'Image_small'

for dir in os.listdir(path_old):
    if len(dir) == 4:
        path = os.path.join(path_new, dir)
        if not os.path.exists(path):
            os.mkdir(path)
            print(f'Папка {path} создана')
        for dirs in os.listdir(os.path.join(path_old, dir)):
            path_dirs = os.path.join(path, dirs)
            if not os.path.exists(path_dirs):
                os.mkdir(path_dirs)
                print(f'Папка {path_dirs} создана')
'''
for dir in os.listdir(path_old):
    if len(dir) == 4:
        for dirs in os.listdir(os.path.join(path_old, dir)):
            dir_old = os.path.join(path_old, dir, dirs)
            for file in os.listdir(dir_old):
                file_old = os.path.join(dir_old, file)
                file_new = os.path.join(path_new, file_old[7:])
                image = Image.open(file_old)
                new_size = 640, 360
                image.thumbnail(new_size, reducing_gap=None)
                image.save(file_new)
                print(f'Создан файл {file_new}')
'''
path_old = 'Images/2023'
for dir in os.listdir(path_old):
            dir_old = os.path.join(path_old, dir)
            print(dir_old)
            for file in os.listdir(dir_old):
                file_old = os.path.join(dir_old, file)
                file_new = os.path.join(path_new, file_old[7:])
                image = Image.open(file_old)
                new_size = 640, 360
                image.thumbnail(new_size, reducing_gap=None)
                image.save(file_new)
                print(f'Создан файл {file_new}')



