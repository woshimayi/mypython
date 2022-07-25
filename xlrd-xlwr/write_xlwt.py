import xlwt

workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = workbook.add_sheet('test', cell_overwrite_ok=True)



# for i in range(24):
# 	sheet = workbook.add_sheet('url_'+str(i), cell_overwrite_ok=True)
# workbook.save(r'./test.xls')

sheet.write(0,0, 'EnglishName')
sheet.write(1,0, 'Marcovaldo')
sheet.write(2,0, 'bill')

txt1 = 'CH_ZH'
sheet.write(0,1, txt1)
txt2 = 'mamma'
sheet.write(1, 1, txt2)
txt2 = 'make'
sheet.write(2, 1, txt2)

workbook.save(r'./test.xls')
