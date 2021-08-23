import openpyxl
import os
import xlrd, xlwt
from xlrd import open_workbook
from xlutils.copy import copy
from tkinter import *

def consol():
    wb = openpyxl.Workbook()
    wb.save('DataBase.xls')
    filename = os.listdir(".")
    filename.remove('Consol_xls.py')
    filename.remove('DataBase.xls')
    s = 0
    a = 0
    b = 0
    while s<len(filename):
        rb = xlrd.open_workbook(filename[s])
        sheet = rb.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols
        book = open_workbook('DataBase.xls')
        wb = copy(book)
        sheet_book = wb.get_sheet('Sheet')
        for i in range(1,nrows,1):
            for j in range(0,ncols,1):
                val = sheet.row_values(i)[j]
                sheet_book.write(a,b,val)
                b=b+1
            a=a+1
            b=0
        wb.save('DataBase.xls') 
        print(filename[s])
        s = s+1
    if s == len(filename):
        label = Label(window, text = "Объединение завершено")
        label.grid(column = 0, row = 5)
        
window = Tk()
window.title("XLS Combining")
window.geometry("500x250")
lbl_1 = Label(window, text="Правила использования:")
lbl_1.grid(column=0, row=0)
lbl_2 = Label(window, text="1. Все файлы должны иметь расширение .xls")
lbl_2.grid(column=0, row=1)
lbl_3 = Label(window, text="2. В директории присутствуют только необходимые .xls-файлы и программа Consol.py")
lbl_3.grid(column=0, row=2)
lbl_4 = Label(window, text="3. Наименование файлов не содержит Кириллицы")
lbl_4.grid(column=0, row=3)  
btn = Button(text="Объединить",background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=consol)
btn.grid(column=0, row=4)  

window.mainloop()
