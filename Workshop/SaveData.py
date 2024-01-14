from MySaveLoad import load_pkl, save_pkl
import torch
import os

# Загружаем нужные нам индексы
index1 = load_pkl('NP-Image/list_index1.pkl')
index2 = load_pkl('NP-Image/list_index1.pkl')
index3 = load_pkl('NP-Image/list_index1.pkl')

# Загружаем базу обучения
train = load_pkl('NP-Image/image.pkl')/255
train = torch.from_numpy(train.transpose(0, 3, 1, 2)).type(torch.float32)

# Сохранение целевых картинок
save_pkl('NP-Image/image1.pkl', train[index1[-1]])
save_pkl('NP-Image/image2.pkl', train[index2[-1]])
save_pkl('NP-Image/image3.pkl', train[index3[-1]])

#Создание списка новых картинок
train = load_pkl('NP-Image/images_orig.pkl')
result1 = [train[i] for i in index1]
result2 = [train[i] for i in index2]
result3 = [train[i] for i in index3]

#Сохранение новых картинок в итоговом датасете
if os.path.exists("DataSet/image1.pkl"):
    basicSet1 = load_pkl("DataSet/image1.pkl")
    basicSet2 = load_pkl("DataSet/image2.pkl")
    basicSet3 = load_pkl("DataSet/image2.pkl")
    basicSet1 += result1
    basicSet2 += result2
    basicSet3 += result3
    print(f'количество файлов в датасете - {len(basicSet1)}')
    save_pkl("DataSet/image1.pkl", basicSet1)
    save_pkl("DataSet/image2.pkl", basicSet2)
    save_pkl("DataSet/image3.pkl", basicSet3)
else:
    save_pkl("DataSet/image1.pkl", result1)
    save_pkl("DataSet/image2.pkl", result2)
    save_pkl("DataSet/image3.pkl", result3)

#Удаление ненужных датасетов
os.remove('NP-Image/image.pkl')
os.remove('NP-Image/images_orig.pkl')





