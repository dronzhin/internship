'''
Есть предположение, что на черно-белой, результаты могут быть лучше или по крайне мере такими же, а размер уменьшится в
3 раза. На данном этапе просто посмотрим, как визуально изменится картинка.
Подготовим картинки размера (640, 360, 3) и сравним цветную и черно-белую. Берем 500, 1500, 2500, 3500, 4500 картинки.
'''
import cv2
import numpy as np
from My_functions import show_images

width = 640
height = 360
video_path = 'C:/Users/mrakr/Internship/Video/Data/20_04_18.MOV'

cap = cv2.VideoCapture(video_path)
num_cap = [500, 1500, 2500]
cap_orig = []
cap_grey = []

for i in num_cap:
  cap.set(cv2.CAP_PROP_POS_FRAMES, i)
  _, frame_orig = cap.read()

  frame = cv2.resize(frame_orig, (width, height))
  np_frame = np.array(frame)
  cap_orig.append(np_frame)

  frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  np_frame = np.array(frame_grey)
  cap_grey.append(np_frame)

show_images(cap_orig, cap_grey, num_cap)
print(cap_grey[0].shape)