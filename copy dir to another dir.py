# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re
from shutil import copyfile
f=open('list.txt')
line= f.readline().rstrip()
while line:
    name = line
    if os.path.isdir(name):
        if os.path.isdir('art'+'/'+line):
            line = line + '_add'
            
        shutil.copytree(name,'art'+'/'+line)
    line = f.readline().rstrip()
f.close()
