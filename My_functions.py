import time
import psutil
import matplotlib.pyplot as plt

# Функция определении времени работы кода
class timex:
    def __enter__(self):
        # Фиксация времени старта процесса
        self.t = time.time()
        return self
    def __exit__(self, type, value, traceback):
        # Вывод времени работы
        print('Время обработки: {:.2f} с'.format(time.time() - self.t))

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