# Цель эксперименты:
# 1. Проверить как будет обрабатываться видел в jolo
# 2. Посмотреть результаты работы на всех подедях jolo
from ultralytics import YOLO
from My_functions import get_all_files_in_directory
from PIL import Image
import matplotlib.pyplot as plt

model = YOLO('yolov8x.pt')
dir = 'C:\\internship\\Full_Model\\Images\\2022\\01-13-22'
files_path = get_all_files_in_directory(dir)
res = model(files_path[340:350])[7]
res = Image.fromarray(res.plot()[:, :, ::-1])
plt.imshow(res)
plt.show()