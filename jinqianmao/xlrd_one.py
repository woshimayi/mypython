# code=UTF-8

import xlrd


# open excl
data   = xlrd.open_workbook(r"/home/zs/Documents/MAC_20180804.xlsx")

# open sheet
table1 = data.sheets()[0]
print(table1)
# table2 = data.sheet_by_index(0)
# print(table2)
# table3 = data.sheet_by_name(u'Sheet1')
# print(table3)

# get nrwos ncols 
nrows = table1.nrows
ncols = table1.ncols
# print("%d\n %d" % (nrows, ncols))


# get row cols value
rows = table1.row_values(0)
cols = table1.col_values(1)
# print("rows:%s\nnols:%s\n" % (rows, cols))

# get cell value
cell_A1 = table1.cell_value(0,0)
cell_C4 = table1.cell_value(3,2)
print("A1:%s\nC4:%s" % (cell_A1, cell_C4))

# get row column value
cell_A1 = table1.row(0)[0].value
cell_C4 = table1.col(2)[3].value
print("A1:%s\nC4:%s\n" % (cell_A1, cell_C4))