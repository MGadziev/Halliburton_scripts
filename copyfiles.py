import os
import shutil
import csv
import re

f=open('list.txt')
line= f.readline().rstrip()
from shutil import copyfile
while line:
    copyfile('1.msg',line +'.msg')
    line= f.readline().rstrip()
f.close()
