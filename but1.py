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
    ccd=filename[len(filename)-21:]
    mta=filename[len(filename)-30:len(filename)-21]
    dir_name=ccd[0:8]+'_'+ccd[8:14]+'_'+ccd[14:21]+'_'+mta
    file_name=ccd[0:8]+'_'+ccd[8:14]+'_'+ccd[14:21]+'_'+mta
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    while os.path.isfile(dir_name+'/'+file_name+file_extension):
        file_name=file_name+'_add'
    shutil.move(line,dir_name+'/'+file_name+file_extension)
    line=f.readline().rstrip()

f.close()
