# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('2018.txt')
line= f.readline().rstrip()
while line:
    filename = line[16:23]+ '.pdf'
    if os.path.isfile(filename):
        if not os.path.isdir(line):
            os.makedirs(line)
        if os.path.isfile(line+'/'+filename+'.pdf'):
            filename=re.sub('.pdf','',filename)
            filename=filename+'_add'
        shutil.move(filename, line+'/'+filename)
    line=f.readline().rstrip()

f.close()
