# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
while line:
    filename = line[0:23]+ '.xls'
    if os.path.isfile(filename):
        while os.path.isfile(line+ '/'+filename):
            filename = re.sub('.xls','',filename)
            filename= filename+ '_add'+'.xls'
        shutil.move(filename, line +'/'+filename)
    line=f.readline().rstrip()

f.close()
