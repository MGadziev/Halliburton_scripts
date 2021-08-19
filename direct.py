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
    i=0
    from shutil import copyfile
    while i<=len(filename):
        if i==21:
            copyfile(line, filename[0:21]+file_extension)
        if i==42:
            copyfile(line, filename[21:42]+file_extension)
        if i==63:
            copyfile(line, filename[42:63]+file_extension)
        if i==63:
            copyfile(line, filename[63:84]+file_extension)
        if i==84:
            copyfile(line, filename[84:105]+file_extension)
        if i==126:
            copyfile(line, filename[105:126]+file_extension)
        if i==147:
            copyfile(line, filename[126:147]+file_extension)
        if i==168:
            copyfile(line, filename[147:168]+file_extension)
        i=i+1
    line=f.readline().rstrip()

f.close()
