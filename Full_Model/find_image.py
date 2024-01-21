from Line_space import find_image
import matplotlib.pyplot as plt
from PIL import Image

# Параметры
target_image = 'Image_640-360\\2023\\04-27-23\\120-im-04-27-23-1p.jpg'
dir_images = 'Image_640-360\\2022\\07-13-22'
name_model = 'autoencoder_640-360.pkl'
count = 10
var = 1 # 1 - Манхэттенское расстояние
        # 2 - Эвклидово расстояние
        # 3 - Расстояние Чебышёва

list_dist, list_path = find_image(target_image, dir_images, name_model, count, var)
print(list_dist)
print(list_path)

images = []
for path in list_path:
    image = Image.open(path)
    images.append(image)

figure, axs = plt.subplots(5, 2, figsize=(10, 20))
count = 0
for i in range(5):
    for j in range(2):
        axs[i, j].imshow(images[count])
        count += 1
plt.show()
