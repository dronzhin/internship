'''
Можно попробовать использовать более высокую детализацию, но разбить картинку на несколько картинов и обучать на частях,
а не на целой картинке, а потом объединять информацию
Попробуем взять две картинки и разбить их на 9 частей, на в итоге должны получить 18 картинок
'''

import cv2
from My_functions import cut_patrs, show_part

width = 1920
height = 1080
video_path = 'C:/Users/mrakr/Internship/Video/Data/20_04_18.MOV'

cap = cv2.VideoCapture(video_path)

# Загрузка 1000 картинки
cap.set(cv2.CAP_PROP_POS_FRAMES, 1000)
_, frame1 = cap.read()
frame1 = cv2.resize(frame1, (width, height))
import torch

# Загрузка 2000 картинки
cap.set(cv2.CAP_PROP_POS_FRAMES, 2000)
_, frame2 = cap.read()
frame2 = cv2.resize(frame2, (width, height))

# Разрезаем картинку на части
new_frame1 = cut_patrs(frame1, (2, 3), (height, width))
new_frame2 = cut_patrs(frame2, (5, 5), (height, width))

# Показываем разрезанные картики
show_part(new_frame1, (2, 3))
show_part(new_frame2, (5, 5))