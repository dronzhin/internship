import os
from My_functions import timex
import cv2

path_videos = []
PATH_VIDEO = 'Video/'
for video in os.listdir(PATH_VIDEO):
  name = os.path.join(PATH_VIDEO, video)
  path_videos.append(name)
print(path_videos)

PATH_IMAGE = '2021/'
for i in path_videos:
    path = PATH_IMAGE + i[6:14]
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Папка {i[6:14]} успешно создана")

name_path = ''
with timex():
  n = 0
  for i in range(len(path_videos)):
    print(path_videos[i])
    with timex():
      cap = cv2.VideoCapture(path_videos[i])
      fps = round(cap.get(5), 2)
      if name_path != path_videos[i][6:14]:
        frame_number = 1
        name_path = path_videos[i][6:14]
      while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            k = 1
            if path_videos[i][6:-4] == '09-21-19' and frame_number == 253:
                k = 2
            if path_videos[i][6:-4] == '04-16-19' and frame_number == 465:
                k = 2
            if path_videos[i][6:-4] == '04-16-19' and frame_number == 480:
                k = 2
            name = f'{frame_number}-im_{path_videos[i][6:-4]}.jpg'
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + fps * k)
            frame_number += 1
            image_path = f'{PATH_IMAGE}{path_videos[i][6:14]}/{name}'
            cv2.imwrite(image_path, frame)
            print(f'Картинка {name} загружена')
        else:
            n += 1
            print(f'{n} видео добавлено')
            print(f'Формат видео ({int(cap.get(3))}, {int(cap.get(4))}, 3), fps ({fps}) - получено {frame_number - 1} картинок')
            cap.release()
            break

