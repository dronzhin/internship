import cv2
import gc
import numpy as np
from My_functions import timex

video_path = 'C:/Users/mrakr/Internship/Video/Data/20_04_18.MOV'
cap = cv2.VideoCapture(video_path)
fps = cap.get(5)
width = cap.get(3)
height = cap.get(4)
# Массив с новыми размерами
size_cap = [(int(width//2), int(height//2)), (int(width//3), int(height//3)), (int(width//4), int(height//4)), (int(width//8), int(height//8))]

# Создадим массив картинок под разные размеры
frames2 = []
frames3 = []
frames4 = []
frames8 = []
frames_all = [frames2, frames3, frames4, frames8]
for i in range(4):
    with timex():
      if cap.isOpened(): cap.release()
      gc.collect()
      cap = cv2.VideoCapture(video_path)
      while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Преобразуем кадр в RGB формат
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Изменяем размер и добавляем кадр в массив
            frame = cv2.resize(frame, size_cap[i])
            frames_all[i].append(frame)
            # Перемещаемся к следующему кадру
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + fps)
        else:
            break
      print(f'Перевод в формат {size_cap[i]}:')
cap.release()

np_frames_all = []
for i in range(4):
  gc.collect()
  # Преобразование массива в numpy массив
  np_frames = np.array(frames_all[i])
  np_frames_all.append(np_frames)
  # Вывод размера массива

  print(np_frames_all[i].shape)
  size = round(np_frames_all[i].nbytes/1024/1024/1024, 4)
  print(f'Занимает {size} гигабайт')
  print(f'Размер картинки занимает {round(size * 1024 / 331, 2)} мб')
  print()

'''
Перевод в формат (1920, 1080):
Время обработки: 135.25 с
Перевод в формат (1280, 720):
Время обработки: 133.96 с
Перевод в формат (960, 540):
Время обработки: 134.55 с
Перевод в формат (480, 270):
Время обработки: 133.62 с
(331, 1080, 1920, 3)
Занимает 1.9177 гигабайт
Размер картинки занимает 5.93 мб

(331, 720, 1280, 3)
Занимает 0.8523 гигабайт
Размер картинки занимает 2.64 мб

(331, 540, 960, 3)
Занимает 0.4794 гигабайт
Размер картинки занимает 1.48 мб

(331, 270, 480, 3)
Занимает 0.1199 гигабайт
Размер картинки занимает 0.37 мб
'''