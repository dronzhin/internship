from MySaveLoad import load_pkl
import torch
import torch.nn as nn
from My_functions import timex
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Загружаем базу и переводим в torch
train = load_pkl('NP-Image/image.pkl')/255
train = torch.from_numpy(train.transpose(0, 3, 1, 2)).type(torch.float32)
print(train.shape)

# Dataset Loader (подготовка данных для сети)
trainLoader = torch.utils.data.DataLoader(dataset=train,
                                          batch_size=32,
                                          shuffle=True)
# Загрузка модели и настройка параметров
autoencoder = torch.load('autoencoder.pkl')
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(autoencoder.parameters(), lr=0.00001)
losses = [] # сюда будет добавляться средняя ошибка. Список будем использовать для построения графика
autoencoder.train() # переход в режим обучения

# Запуск обучения
epochs = 20
for epoch in range(epochs):
    with timex():
        for i, images in enumerate(trainLoader):
            images = images.to(device)
            optimizer.zero_grad()  # обнуляем градиент
            outputs = autoencoder(images)  # делаем предсказание
            loss = criterion(outputs, images)  # считаем ошибку
            loss.backward()  # обратное распространение ошибки
            optimizer.step()  # шаг оптимизации

        print('Эпоха: [%d/%d], Ошибка: %.4f'
                      % (epoch + 1, epochs, loss))

# Сохранение модели
torch.save(autoencoder, 'autoencoder.pkl')