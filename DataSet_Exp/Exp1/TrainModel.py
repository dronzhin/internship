import pickle as pkl
import torch
import torch.nn as nn
from My_functions import timex
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Загружаем базу и переводим в torch
with open(f'../data10.pkl', "rb") as f:
    train = pkl.load(f)
train = torch.from_numpy(train.transpose(0, 3, 1, 2))

# Dataset Loader (подготовка данных для сети)
trainLoader = torch.utils.data.DataLoader(dataset=train,
                                          batch_size=32,
                                          shuffle=True)

autoencoder = torch.load('autoencoder_exp1.pkl')
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(autoencoder.parameters(), lr=0.0001)
losses = [] # сюда будет добавляться средняя ошибка. Список будем использовать для построения графика
autoencoder.train() # переход в режим обучения
for epoch in range(10):
    with timex():
        for i, images in enumerate(trainLoader):
            images = images.to(device)
            optimizer.zero_grad()  # обнуляем градиент
            outputs = autoencoder(images)  # делаем предсказание
            loss = criterion(outputs, images)  # считаем ошибку
            loss.backward()  # обратное распространение ошибки
            optimizer.step()  # шаг оптимизации

        print('Эпоха: [%d/%d], Шаг: [%d/%d], Ошибка: %.4f'
                      % (epoch + 1, 10, i + 1, len(train) // 32, loss))
torch.save(autoencoder, 'autoencoder_exp1.pkl')
torch.cuda.empty_cache()