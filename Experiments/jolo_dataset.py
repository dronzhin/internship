from My_functions import get_all_files_in_directory, create_list_files
import zipfile
import os
import shutil

dir_image_path = 'buildings_2023'
path_box = 'C:\internship\Experiments\\box2023'
dir = 'obj_train_data'

list_path_image = get_all_files_in_directory(dir_image_path)
list_rar_path = create_list_files(path_box)
list_path = create_list_files(dir_image_path)
list_path_short = [x[15:] for x in list_path]
print(list_path)

for i in range(len(list_path)):
    with zipfile.ZipFile(list_rar_path[i], 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.startswith(dir + '/'):
                zip_ref.extract(file_info, os.path.join(path_box, list_path_short[i]))




