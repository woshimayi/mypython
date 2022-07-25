import xlrd
import xlutils.copy

data = xlrd.open_workbook(r'./test.xls')
ws = xlutils.copy.copy(data)
table = ws.get_sheet(0)

table.write(0,3, 'D1')
ws.save(r'./test.xls')