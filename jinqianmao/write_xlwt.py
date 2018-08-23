import xlwt

workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = workbook.add_sheet('test', cell_overwrite_ok=True)

sheet.write(0,0, 'EnglishName')
sheet.write(1,0, 'Marcovaldo')
txt1 = 'CH_ZH'
sheet.write(0,1, txt1)
txt2 = 'mamma'
sheet.write(1, 1, txt2)

workbook.save(r'./test.xlsx')