# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
while line:

    filename, file_extension = os.path.splitext(line)
    filename=re.sub('_','',filename)
    filename=re.sub(' ','',filename)
    filename=re.sub('-','',filename)
    dir_name = filename
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    while os.path.isfile(dir_name+'/'+filename+file_extension):
        filename=filename+'_add'
    shutil.move(line,dir_name+'/'+filename+file_extension)
    line=f.readline().rstrip()

f.close()
