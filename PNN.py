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
    dir_name= filename[0:8]+'_'+filename[8:14]+'_'+filename[14:21]+'_'+filename[len(filename)-9:len(filename)-6]+'-'+filename[len(filename)-6:]
    file_name= filename[0:8]+'_'+filename[8:14]+'_'+filename[14:21]+'_'+filename[len(filename)-9:len(filename)-6]+'-'+filename[len(filename)-6:]
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    while os.path.isfile(dir_name+'/'+file_name+file_extension):
        file_name=file_name+'_add'
    shutil.move(line,dir_name+'/'+file_name+file_extension)
    line=f.readline().rstrip()

f.close()
