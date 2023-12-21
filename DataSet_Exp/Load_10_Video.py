'''
Загрузим 10 видео и разобьем его на картинки 1 картинка 3 секунда. Размер картинки (640, 360, 3)
'''

import os
import cv2
import gc
import matplotlib.pyplot as plt
import pickle as pkl
from My_functions import timex, Memory_Usage
import numpy as np

PATH_VIDEO = 'C:/Users/mrakr/Internship/Video/orig/'

# Создаем массив путей файлов
path_videos = []
for video in os.listdir(PATH_VIDEO):
  name = os.path.join(PATH_VIDEO, video)
  path_videos.append(name)
print(path_videos)

with timex():
  images = []
  gc.collect()
  print('Начальное состояние')
  Memory_Usage()
  n = 0
  for video in path_videos:
    print()
    print(video)
    with timex():
      cap = cv2.VideoCapture(video)
      fps = round(cap.get(5), 2)
      num = 0
      while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 360))
            images.append(frame)
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + fps * 2)
            num += 1
        else:
            n += 1
            print(f'{n} видео добавлено')
            print(f'Формат видео ({int(cap.get(3))}, {int(cap.get(4))}, 3), fps ({fps}) - получено {num} картинок, формата (640, 360, 3))')
            Memory_Usage()
            cap.release()
            break
images = np.array(images)
# Сжатие диапазона [0, 255] значений к диапазону [0, 1]
images = images.astype('float32') / 255.
print()
gc.collect()
print('Использовался gc.collect()')
Memory_Usage()
plt.imshow(images[6])
plt.show()

with open('data10.pkl', "wb") as f: # Открывем файл в формате чтение и запись
    pkl.dump(images, f)           # Записываем сериализованный объект

'''
['C:/Users/mrakr/Internship/Video/orig/11_01_19_1.MP4', 'C:/Users/mrakr/Internship/Video/orig/11_01_19_2.MP4', 'C:/Users/mrakr/Internship/Video/orig/11_07_20_1.MP4', 'C:/Users/mrakr/Internship/Video/orig/11_07_20_2.MP4', 'C:/Users/mrakr/Internship/Video/orig/13_07_19_1.MOV', 'C:/Users/mrakr/Internship/Video/orig/13_07_19_2.MOV', 'C:/Users/mrakr/Internship/Video/orig/18_01_20_2.MP4', 'C:/Users/mrakr/Internship/Video/orig/1var.pkl', 'C:/Users/mrakr/Internship/Video/orig/20_04_18.MOV']
Начальное состояние
Объем оперативной памяти, занимаемый выполнением кода: 62.34 мб

C:/Users/mrakr/Internship/Video/orig/11_01_19_1.MP4
1 видео добавлено
Формат видео (1920, 1080, 3), fps (23.98) - получено 260 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 338.89 мб
Время обработки: 28.60 с

C:/Users/mrakr/Internship/Video/orig/11_01_19_2.MP4
2 видео добавлено
Формат видео (1920, 1080, 3), fps (23.98) - получено 82 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 391.72 мб
Время обработки: 9.09 с

C:/Users/mrakr/Internship/Video/orig/11_07_20_1.MP4
3 видео добавлено
Формат видео (2688, 1512, 3), fps (25.0) - получено 161 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 583.58 мб
Время обработки: 42.34 с

C:/Users/mrakr/Internship/Video/orig/11_07_20_2.MP4
4 видео добавлено
Формат видео (2688, 1512, 3), fps (25.0) - получено 98 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 648.08 мб
Время обработки: 26.94 с

C:/Users/mrakr/Internship/Video/orig/13_07_19_1.MOV
5 видео добавлено
Формат видео (2720, 1530, 3), fps (25.0) - получено 167 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 767.56 мб
Время обработки: 45.60 с

C:/Users/mrakr/Internship/Video/orig/13_07_19_2.MOV
6 видео добавлено
Формат видео (2720, 1530, 3), fps (25.0) - получено 70 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 820.55 мб
Время обработки: 19.06 с

C:/Users/mrakr/Internship/Video/orig/18_01_20_2.MP4
7 видео добавлено
Формат видео (2688, 1512, 3), fps (25.0) - получено 161 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 904.63 мб
Время обработки: 39.68 с

C:/Users/mrakr/Internship/Video/orig/1var.pkl
Время обработки: 0.39 с

C:/Users/mrakr/Internship/Video/orig/20_04_18.MOV
8 видео добавлено
Формат видео (3840, 2160, 3), fps (25.0) - получено 169 картинок, формата (640, 360, 3))
Объем оперативной памяти, занимаемый выполнением кода: 1193.2 мб
Время обработки: 69.43 с
Время обработки: 281.14 с

Использовался gc.collect()
Объем оперативной памяти, занимаемый выполнением кода: 858.04 мб
'''