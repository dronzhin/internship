from My_functions import timex
from My_Models import model_check
import pickle as pkl
import numpy as np
import torchvision
import My_Models
import matplotlib.pyplot as plt
from My_Models import on_epoch_end

shape = 360, 640, 3
PATH_VIDEO = 'Internship/Video/orig/'
with open(f'data10.pkl', "rb") as f: # Открываем файл для чтения
    train = pkl.load(f)     # Загружаем объект из файла

autoencoder = My_Models.Model_autoencoder_Conv(shape)
print(train.shape)