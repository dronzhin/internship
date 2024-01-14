import gdown
import pickle as pkl


# Функция загрузки файлов по ссылке URL
def load_urls(*args):
    try:
        for i in args:
            gdown.download(i, quiet=True)
        print("Файлы успешно загружены")
    except Exception as e:
        print(f"Ошибка при загрузке файлов: {e}")


# Функция сохранения данных в формате Pickle
def save_pkl(path, data):
    with open(path, "wb") as f:
        pkl.dump(data, f)
    print(f'Сохранение {path} прошло успешно')


# Функция загрузки данных из формата Pickle
def load_pkl(path):
    try:
        with open(path, "rb") as f:
            data = pkl.load(f)
        print('Загрузка произведена успешно')
        return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
