# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
while line:
    if os.path.isdir(line):
        print (line)
f.close()
