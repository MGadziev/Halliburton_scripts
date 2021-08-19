# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('DME.txt')
line= f.readline().rstrip()
while line:
    if os.path.isfile(line[16:23]+'.msg'):
        os.makedirs(line)
        shutil.move(line[16:23]+'.msg', line+'/'+line[16:23]+'.msg')
    line=f.readline().rstrip()

f.close()
