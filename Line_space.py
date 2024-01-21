from PIL import Image
from torchvision import transforms
import torch
import os
import numpy as np
def find_image(target_image, path_dir, model, count, var):

    # 1 Блок. Подготовка целевой картинки
    try:
        image = Image.open(target_image)
        print(f'Загрузка целевой картинки {target_image} произведена успешно')
    except Exception as e:
        print(f"Ошибка при картинки: {e}")
    preprocess = transforms.Compose([
        transforms.ToTensor()
    ])
    image = preprocess(image).unsqueeze(0)

    # 2 Блок. Загрузка модели и предсказание целевой картинки
    try:
        autoencoder = torch.load(model).to('cpu')
        print(f'Модель {model} загружена')
    except Exception as e:
        print(f"Ошибка при загрузке модели: {e}")
    _, target_line = autoencoder(image)

    # 3 Блок. Нахождение растояния
    list_of_path = []
    list_of_dist = []
    for path in os.listdir(path_dir):
        path = os.path.join(path_dir, path)
        list_of_path.append(path)
        image = Image.open(path)
        image = preprocess(image).unsqueeze(0)
        _, line = autoencoder(image)
        if var == 3: var = float('inf')
        dist = torch.dist(target_line[0], line[0], p=var)
        list_of_dist.append(dist.item())
    list_of_index = np.argsort(np.array(list_of_dist))
    list_of_dist = [list_of_dist[i] for i in list_of_index]
    list_of_path = [list_of_path[i] for i in list_of_index]
    return list_of_dist[:count], list_of_path[:count]