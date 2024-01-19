from MySaveLoad import load_pkl
from My_functions import timex
import torchvision.transforms as transforms
from PIL import Image
import torch
import torch.nn as nn
import random
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

PATHS = 'list_of_path_image_640-360.pkl'
number_of_images = 1000
batch_size = 20
count_batch = number_of_images/batch_size


list_of_files = load_pkl(PATHS)
random.shuffle(list_of_files)
new_list = []
number_parts = len(list_of_files) // number_of_images + 1
for i in range(number_parts):
    if i == 0:
        list = list_of_files[:number_of_images]
    elif i == number_parts - 1:
        list = list_of_files[number_of_images * i:]
    else:
        list = list_of_files[(number_of_images * i) : (number_of_images * (i + 1))]
    new_list.append(list)

# autoencoder = torch.load('autoencoder_new.pkl').to(device)
autoencoder = torch.load('autoencoder_640-360.pkl')
# autoencoder = torch.load('autoencoder.pkl')
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(autoencoder.parameters(), lr=0.0001)

for epoch in range(1):
    with timex():
        # Преобразование изображений в тензоры PyTorch
        transform = transforms.Compose([
            transforms.ToTensor()  # Преобразование изображений в тензоры
        ])
        loss_epoch = 0
        count = 0
        for image_paths in new_list:
            count += 1
            tensor_list = []
            loss_numbers = 0
            with timex():
                for image_path in image_paths:
                    image = Image.open(image_path)
                    tensor = transform(image)  # Преобразование изображения в тензор
                    tensor_list.append(tensor)
                trainLoader = torch.utils.data.DataLoader(dataset=tensor_list,
                                                              batch_size=batch_size,
                                                              shuffle=True)
                for i, images in enumerate(trainLoader):
                    images = images.to(device)
                    optimizer.zero_grad()  # обнуляем градиент
                    outputs, _ = autoencoder(images)  # делаем предсказание
                    loss = criterion(outputs, images)  # считаем ошибку
                    print(f'ошибка батча - {loss.type(torch.float16)}')
                    loss_numbers += loss
                    loss.backward()  # обратное распространение ошибки
                    optimizer.step()  # шаг оптимизации
                loss_numbers = loss_numbers/count_batch
                print(f'ошибка пула картинок - {loss_numbers.type(torch.float16)}')
                loss_epoch += loss_numbers
                break
        loss_epoch = loss_epoch/count
        print('---' * 10)
        print(f'ошибка эпохи - {loss_epoch.type(torch.float16)}')
        print('---' * 10)
torch.save(autoencoder, 'autoencoder_640-360.pkl')







