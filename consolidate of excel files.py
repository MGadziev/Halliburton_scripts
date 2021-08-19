import xlrd, xlwt
from xlrd import open_workbook
from xlutils.copy import copy
f=open('list.txt')
line = f.readline().rstrip()
a=0
b=0
while line:
    rb = xlrd.open_workbook(line,formatting_info=True)
    sheet = rb.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    book = open_workbook('test.xls')
    wb = copy(book)
    sheet_book = wb.get_sheet('list')
    for i in range(1,nrows,1):
        for j in range(0,ncols,1):
            val = sheet.row_values(i)[j]
            sheet_book.write(a,b,val)
            b=b+1
        a=a+1
        b=0
    wb.save('test.xls')
    line = f.readline().rstrip()
    

