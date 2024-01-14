import matplotlib.pyplot as plt
import numpy as np
import torch
from My_functions import timex, show_images_list_torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
from MySaveLoad import load_pkl, save_pkl

def show_result(list_dist, image, n):
    list_index = np.argsort(list_dist)[:n]
    list_result = [train[i] for i in list_index]
    image = image.transpose(0, 2).transpose(0, 1)
    plt.imshow(image)
    plt.imshow
    show_images_list_torch(list_result)
    return list_index

# Загружаем базу картинок
with timex():
    train = load_pkl('NP-Image/image.pkl')/255
train = torch.from_numpy(train.transpose(0, 3, 1, 2)).type(torch.float32)

# Загружаем модель и переводим в режим предсказания
autoencoder = torch.load('autoencoder.pkl')
autoencoder.eval()

# Загружаем целевые картинки
image1 = load_pkl('NP-Image/image1.pkl')
image2 = load_pkl('NP-Image/image2.pkl')
image3 = load_pkl('NP-Image/image3.pkl')

# Высчитываю линейное пространство
list_dist1 = []
list_dist2 = []
list_dist3 = []
with timex():
    with torch.no_grad():
        dist1 = autoencoder.encode(image1.unsqueeze(0).to(device)).to('cpu')
        dist2 = autoencoder.encode(image2.unsqueeze(0).to(device)).to('cpu')
        dist3 = autoencoder.encode(image3.unsqueeze(0).to(device)).to('cpu')
        for i in range(train.shape[0]):
            output = autoencoder.encode(train[i].unsqueeze(0).to(device)).to('cpu')
            torch.cuda.empty_cache()
            distance1 = torch.dist(dist1, output, p=2)
            distance2 = torch.dist(dist2, output, p=2)
            distance3 = torch.dist(dist3, output, p=2)
            list_dist1.append(distance1)
            list_dist2.append(distance2)
            list_dist3.append(distance3)

# Проверка найденных картинок
list_index1 = show_result(list_dist1, image1, 5)
list_index2 = show_result(list_dist2, image2, 5)
list_index3 = show_result(list_dist3, image3, 5)

# Сохранение индексов найденных картинок
save_pkl('NP-Image/list_index1.pkl', list_index1)
save_pkl('NP-Image/list_index2.pkl', list_index2)
save_pkl('NP-Image/list_index3.pkl', list_index3)






