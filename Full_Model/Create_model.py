from My_functions import get_all_files_in_directory
from MySaveLoad import save_pkl
from My_Models import Model_autoencoder_Conv
import torch
from PIL import Image
import numpy as np

main_dir = 'Image_640-360'
# main_dir = 'Images'
paths = get_all_files_in_directory(main_dir)
for i in range(100):
    image = Image.open(paths[i + 15000])
    image = np.asarray(image)
    print(image.shape)
save_pkl('list_of_path_image.pkl', paths)

# Создаем модель, устанавливаем ошибку и оптимизатор
autoencoder = Model_autoencoder_Conv()
torch.save(autoencoder, 'autoencoder_new.pkl')

