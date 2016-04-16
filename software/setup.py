from distutils.core import setup
import py2exe
import os

Mydata_files = []
for files in os.listdir('C:/Users/ajans/Documents/workspace/PicoCommander/software/img/'):
    f1 = 'C:/Users/ajans/Documents/workspace/PicoCommander/software/img/' + files
    if os.path.isfile(f1):
        f2 = 'img', [f1]
        Mydata_files.append(f2)

setup(
        data_files = Mydata_files,
        console=['main.py'])
