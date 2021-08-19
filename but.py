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
    dir_name= filename[9:17]+'_'+filename[17:23]+'_'+filename[23:31]+'_'+filename[0:9]
    file_name= filename[9:17]+'_'+filename[17:23]+'_'+filename[23:31]+'_'+filename[0:9]
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    while os.path.isfile(dir_name+'/'+file_name+file_extension):
        file_name=file_name+'_add'
    shutil.move(line,dir_name+'/'+file_name+file_extension)
    line=f.readline().rstrip()


f.close()
