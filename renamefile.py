import os
import shutil


path = './YoWhatsApp Images/'
# files = os.listdir(path)


for files in os.listdir(path):
    if files.endswith('_nomedia'):
        os.rename(os.path.join(path, files), os.path.join(path, files.replace('_nomedia', '')))
    else:
        print('Fucked up')