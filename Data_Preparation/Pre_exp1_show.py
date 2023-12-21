import cv2
from My_functions import show_images
import numpy as np

video_path = 'C:/Users/mrakr/Internship/Video/Data/20_04_18.MOV'
cap = cv2.VideoCapture(video_path)
width = cap.get(3)
height = cap.get(4)

cap.set(cv2.CAP_PROP_POS_FRAMES, 1500)
ret, frame_orig = cap.read()

# Уменьшенные картинки
size_cap = [(int(width//2), int(height//2)), (int(width//3), int(height//3)), (int(width//4), int(height//4)), (int(width//8), int(height//8))]
frame2 = cv2.resize(frame_orig, size_cap[0])
frame3 = cv2.resize(frame_orig, size_cap[1])
frame4 = cv2.resize(frame_orig, size_cap[2])
frame8 = cv2.resize(frame_orig, size_cap[3])

# Подготовка данных
np_frame_orig = np.array(frame_orig)

orig = [np_frame_orig, np_frame_orig, np_frame_orig, np_frame_orig]

np_frame2 = np.array(frame2)
np_frame3 = np.array(frame3)
np_frame4 = np.array(frame4)
np_frame8 = np.array(frame8)

mod = [np_frame2, np_frame3, np_frame4, np_frame8]

names = ['Картинка (1920, 1080, 3)',
         'Картинка (1280, 720, 3)',
         'Картинка (960, 540, 3)',
         'Картинка (480, 270, 3)',]

# Показываем результат
show_images(orig, mod, names, (50, 100))

'''
Как итог мы видим, что уменьшение в 4 раза смотрится смотрибельно, а вот уменьшение в 8 раз заметно влияет визуально на картинку
Попробуем вывести для сравнения картики в 4, 6, 8 раз. И посмотрим на другой картинке 2500
'''

# Созадим новые картики
size_cap = [(int(width//2), int(height//2)), (int(width//3), int(height//3)), (int(width//4), int(height//4)), (int(width//6), int(height//6)), (int(width//8), int(height//8))]

cap.set(cv2.CAP_PROP_POS_FRAMES, 2500)

ret, frame_orig = cap.read()
frame4 = cv2.resize(frame_orig, size_cap[2])
frame6 = cv2.resize(frame_orig, size_cap[3])
frame8 = cv2.resize(frame_orig, size_cap[4])

np_frame_orig = np.array(frame_orig)
np_frame4 = np.array(frame4)
np_frame6 = np.array(frame6)
np_frame8 = np.array(frame8)

orig = [np_frame_orig, np_frame_orig, np_frame_orig]
mod = [ np_frame4, np_frame6, np_frame8]
names = ['Картинка (960, 540, 3)',
         'Картинка (640, 360, 3)',
         'Картинка (480, 270, 3)']

# Показываем результат
show_images(orig, mod, names)

# Уменьшение в 6 раз еще терпимо (640, 360, 3). Сделаем первое предположение, что уменьшение в 6 раз, является пока оптимальным

gc.collect()
cap.release()