import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
from shutil import copyfile
while line:
    
    filename, file_extension = os.path.splitext(line)
    filename=re.sub('-','',filename)
    filename=re.sub('_','',filename)
    filename=re.sub(' ','',filename)
    print(filename[0:7])
    print(filename[7:14])
    print(filename[14:21])
    print(filename[21:28])
    copyfile(line, filename[0:7]+'.msg')
    copyfile(line, filename[7:14]+'.msg')
    copyfile(line, filename[14:21]+'.msg')
    copyfile(line, filename[21:28]+'.msg')

    line= f.readline().rstrip()
f.close()
