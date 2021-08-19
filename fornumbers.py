# -*- coding: utf-8 -*-
import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
while line:
    # удаляем .docx
    line=re.sub('.doc','',line)
    a=line.isalnum()
    if a:
        if not os.path.isdir(line):
            os.makedirs(line)
        shutil.move(line+'.doc',line+'/'+line+ '.doc')
        
    b=re.search('[a-zA-Z]', line)
    c=re.search('[а-яА-Я]', line)
    if (b or c):
        i=0
        while (line[i]=='0' or line[i]=='1' or line[i]=='2' or line[i]=='3' or line[i]=='4' or line[i]=='5' or line[i]=='6' or line[i]=='7' or line[i]=='8' or line[i]=='9'):
            i=i+1
        else:
            if not os.path.isdir(line[0:i]):
                os.makedirs(line[0:i])
            shutil.move(line+'.doc',line[0:i]+'/'+line+'.doc')
    line=f.readline().rstrip()
f.close()
