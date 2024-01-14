import os
from My_functions import create_list_files, timex
from MySaveLoad import save_pkl, load_pkl
import cv2
import numpy as np

# Создаем список видео в папке
path_videos = create_list_files('Video')

# Создаем списки картинок
with timex():
  images = []
  images_orig = []
  n = 0
  for video in path_videos:
    print(video)
    with timex():
      cap = cv2.VideoCapture(video)
      fps = round(cap.get(5), 2)
      num = 0
      while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            images_orig.append(frame)
            frame = cv2.resize(frame, (640, 360))
            images.append(frame)
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + fps * 2)
            num += 1
        else:
            n += 1
            print(f'{n} видео добавлено')
            print(f'Формат видео ({int(cap.get(3))}, {int(cap.get(4))}, 3), fps ({fps}) - получено {num} картинок')
            cap.release()
            break

# Сохранение списков на диске в формате Pickle
images = np.array(images)
images_orig = np.array(images_orig)
save_pkl('NP-Image/image.pkl', images)
save_pkl('NP-Image/images_orig.pkl', images_orig)

'''
['Video\\20_04_18.MOV']
Video\20_04_18.MOV
1 видео добавлено
Формат видео (3840, 2160, 3), fps (25.0) - получено 169 картинок
Время обработки: 69.08 с
Время обработки: 69.08 с
Сохранение NP-Image/image.pkl прошло успешно
Сохранение NP-Image/images_orig.pkl прошло успешно
'''
