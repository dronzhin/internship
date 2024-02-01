import time
import psutil
import matplotlib.pyplot as plt
import os

# Функция создания списка файлов в папке
def create_list_files(path):
    path_files = []
    for file in os.listdir(path):
        name = os.path.join(path, file)
        path_files.append(name)
    print(path_files)
    return path_files
# Функция создания списка файлов в папке и подпапках
def get_all_files_in_directory(root_dir):
    file_list = []
    for root, directories, files in os.walk(root_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
# Функция определении времени работы кода
class timex:
    def __enter__(self):
        # Фиксация времени старта процесса
        self.t = time.time()
        return self
    def __exit__(self, type, value, traceback):
        # Вывод времени работы
        print('Время обработки: {:.2f} с'.format(time.time() - self.t))
def show_images_list_torch(list):
    count = len(list)
    figure, axs = plt.subplots(count, 1, figsize=(25, 15 * count))
    for i in range(count):
        axs[i].set_title(f'{i + 1} картинка')
        axs[i].imshow(list[i].transpose(0, 2).transpose(0, 1))
        axs[i].axis('off')
    plt.show()

# Функция отображения 2 видов картинок
def show_images(orig, mod, names, figsize=(25, 30)):
  count = len(orig)
  if (count != len(mod) and count != len(names)):
    print('Массивы должны одинаковое количество элементов')
    return
  figure, axs = plt.subplots(count, 2, figsize=(25, 30))
  for i in range(count):
        axs[i, 0].set_title('оригинальная картинка')
        axs[i, 0].imshow(orig[i])
        axs[i, 0].axis('off')

        axs[i, 1].set_title(names[i])
        axs[i, 1].imshow(mod[i])
        axs[i, 1].axis('off')
  plt.show()

# Функция нарезки картинок на части
def cut_patrs(img, parts, shape):
  line, column = parts
  step_width = int(shape[1] / column)
  step_height = int(shape[0] / line)

  new_frame = []

  for j in range(line):
    for i in range(column):
      new_frame.append(img[j * step_height : step_height + j * step_height,
                           i * step_width : step_width + i * step_width])
  return new_frame

# Функция отображение нарезанной картинки
def show_part(arr_img, parts):
  line, column = parts
  number = 0
  figure, axs = plt.subplots(line, column, figsize=(50, 30))
  for i in range(line):
    for j in range(column):
        axs[i, j].imshow(arr_img[number])
        number += 1
        axs[i, j].set_title(f'{number} часть картинки')
        axs[i, j].axis('off')
  plt.show()

# Функция отображения оперативной памяти
def Memory_Usage():
    memory_usage = round(psutil.Process().memory_info().rss / 1024 / 1024, 2)
    print(f"Объем оперативной памяти, занимаемый выполнением кода: {memory_usage} мб")

# Отображения оригинальной картинки и предсказанной
def show_orig_pred(orig, pred):
    orig = orig.numpy().transpose(1, 2, 0)
    pred = pred.to('cpu').detach().numpy()[0].transpose(1, 2, 0)
    figure, axs = plt.subplots(1, 2, figsize=(10, 20))

    axs[0].set_title('оригинальная картинка')
    axs[0].imshow(orig)
    axs[0].axis('off')

    axs[1].set_title('Предсказанная')
    axs[1].imshow(pred)
    axs[1].axis('off')
    plt.show()

import supervision as sv
def jolo_convert(arr):
    # Альтернативная визуализация через supervision - только для детекций
    box_annotator = sv.BoxAnnotator(
        thickness=2,  # задает толщину границ рамок, которые будут наложены на изображение с объектами.
        text_thickness=2,  # задает толщину шрифта для надписей, которые будут отображаться внутри рамок с объектами.
        text_scale=1  # масштабирует шрифт для надписей на изображении.
    )

    # получение обнаруженных объектов с помощью функции from_yolov8(res)
    detections = sv.Detections.from_yolov8(res)

    # создание надписей для каждого обнаруженного объекта на изображении
    labels = [
        f"{model.model.names[class_id]} {confidence:0.2f}"
        for _, _, confidence, class_id, _
        in detections
    ]

    # наложение рамок и надписей на изображение
    frame = box_annotator.annotate(
        scene=res.orig_img,  # исходное изображение, на которое будут наложены рамки и надписи.
        detections=detections,  # список обнаруженных объектов в формате, который требуется BoxAnnotator.
        labels=labels  # список надписей для каждого обнаруженного объекта.
    )

    # инвертируем цвет в RGB для отображения
    Image.fromarray(frame[:, :, ::-1])