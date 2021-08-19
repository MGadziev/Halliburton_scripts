# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
while line:

    filename, file_extension = os.path.splitext(line)
    filename=re.sub('-','',filename)
    filename=re.sub('_','',filename)
    filename=re.sub(' ','',filename)
    if 'PNN' in filename:
        index=filename.index('PNN')
        name = filename[0:8]+'_'+filename[8:14]+'_'+filename[14:21]+'_'+filename[index:index+3]+'-'+filename[index+3:index+9]
        dir_name = filename[0:8]+'_'+filename[8:14]+'_'+filename[14:21]+'_'+filename[index:index+3]+'-'+filename[index+3:index+9]
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        while os.path.isfile(dir_name+'/'+name+file_extension):
            name=name+'_add'
        shutil.move(line,dir_name+'/'+name+file_extension)
    line=f.readline().rstrip()

f.close()
