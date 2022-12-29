import os
import shutil
from datetime import datetime

print("Start cleaning Downloads folder")

extension_list = ['txt', 'pdf', 'png', 'JPG', 'gif', 'svg', 'jpg', 'zip', 'gz', 'py', 'xlsx', 'docx', 'exe', 'json', 'rar', 'csv', 'jar', 'yml', 'pptx', 'html', 'msi', 'aia', 'xls', 'ipynb']
file_path = 'C:/Users/joao.junior/Downloads/'

now = datetime.now()
date_time = now.strftime("%d/%m/%Y")
date_time = date_time.replace('/','_')
new_folder_name = 'backup_files_' + date_time

try:
    ath = os.path.join(file_path, new_folder_name)
    os.mkdir(ath)
    print('Create folder for backup: ', ath)
except:
    ath = os.path.join(file_path, new_folder_name)
    print('Erro in backup folder: ', ath)
    
for ext in extension_list:

    try:
        new = os.path.join(ath, ext)
        os.mkdir(new)
        print('Create folder to extension: ', ath)
    except:
        new = os.path.join(ath, ext)
        print('Erro extension folder: ', new)


for extension in extension_list:
    arr = [f for f in os.listdir(file_path) if f.endswith('.'+extension)]
    for file in arr:
        file_from = file_path + file
        file_to = file_path + new_folder_name + '/' + extension + '/' +file
        shutil.move(file_from, file_to)