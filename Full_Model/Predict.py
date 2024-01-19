import torch
import pickle as pkl
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np

# Проверяем, подключена ли видеокарта
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Загружаем модель
name_model = 'autoencoder_640-360.pkl'
try:
    autoencoder = torch.load(name_model)
    print(f'Модель {name_model} загружена')
except Exception as e:
    print(f"Ошибка при загрузке модели: {e}")

# Загружаем список путей к файлам
path = 'list_of_path_image_640-360.pkl'
try:
    with open(path, "rb") as f:
        list_of_path = pkl.load(f)
    print('Загрузка списка путей произведена успешно')
except Exception as e:
    print(f"Ошибка при загрузке файла: {e}")

# Загрузка изображения (Картинки 101)
path_image = list_of_path[65000]
try:
    image = Image.open(path_image)
    print(f'Загрузка картинки {path_image} произведена успешно')
except Exception as e:
    print(f"Ошибка при картинки: {e}")

# Переводим модель в состояние предсказания и подключаем к видеокарте при возможности
autoencoder.eval().to(device)

# Подготоваливаем картинку для подачи в модель
preprocess = transforms.Compose([   # Переводит в торч, меняет формат осей на 3-360-640 с формата 640-360-3
    transforms.ToTensor()
])
image = preprocess(image).unsqueeze(0) # Добавляем торч в список, т.к. модель принимает списки

# .unsqueeze(0) не нужно, если у нас не одна картинка, а список нескольких
image = image.to(device)       # Переводим картинку на видеокарту при возможности
print(image.shape)             # Должен вывести формат torch.Size([1, 3, 360, 640])

# Делаем предсказание
predict, _ = autoencoder(image)
print(predict.shape)


# Объединим две картинки в одну, чтобы вывести одну картинку для проверки
image = image[0].permute(1, 2, 0) #Меняем местами оси, 3 ставим на конец
predict= predict[0].permute(1, 2, 0)
result_image = torch.cat([image, predict], dim=0)
print(result_image.shape)

# Посмотрим результат
result_image = result_image.cpu().detach().numpy()
print(type(result_image))
plt.imshow(result_image)
plt.show()

