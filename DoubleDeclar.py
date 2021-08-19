import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
from shutil import copyfile
while line:
    filename=re.sub(' ','',line)
    a=filename[0:21]+filename[42:51]
    b=filename[21:42]+filename[51:60]
    copyfile(line,a+'.msg')
    copyfile(line,b+'.msg')
    line= f.readline().rstrip()
f.close()
