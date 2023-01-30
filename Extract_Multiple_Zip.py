# -*- coding: utf-8 -*-
import gzip as gz
import os
import zipfile
PATH = '/path/to/zip_files/'
os.chdir(PATH)
FNAMES = os.listdir(PATH)
for i, j in enumerate(FNAMES):
    filename, file_extension = os.path.splitext(str(j))
    if file_extension == '.zip':
        x = zipfile.ZipFile(j)
        x.extractall(PATH + filename)
        x.close()
        print(filename)
    else:
        continue