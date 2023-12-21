import cv2
import numpy as np
import pickle as pkl

import My_functions

# открытие видео
video_path = 'C:/Users/mrakr/Internship/Video/Data/20_04_18.MOV'
cap = cv2.VideoCapture(video_path)
fps = cap.get(5)
width = cap.get(3)
height = cap.get(4)
print(f'Частота кадров в секунду {fps}')
print(f'Размер изображения. Ширина {width}, Высота {height}')
print(f'Общее количество кадров в видео {cap.get(7)}')

# Создадим массив картинок
with My_functions.timex():
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Преобразуем кадр в RGB формат
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Добавляем кадр в массив
            frames.append(frame)
            # Перемещаемся к следующему кадру
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + fps)
        else:
            break
    print('Формирование массива картинок заняло:')
# Преобразование массива в numpy массив
with My_functions.timex():
    np_frames = np.array(frames)
    print('Перевод картинок в np массив занял')
del frames
# Вывод размера массива
print(np_frames.shape)
print(f'Занимает {round(np_frames.nbytes/1024/1024/1024, 2)} гигабайт')
cap.release()
with open('C:/Users/mrakr/Internship/Video/Data/first.pkl', "wb") as f: # Открывем файл в формате чтение и запись
    pkl.dump(np_frames, f)                                              # Записываем сериализованный объект
del np_frames
