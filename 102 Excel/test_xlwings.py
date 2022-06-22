import xlwings as xw

# wb = xw.Book()  # this will create a new workbook
# wb = xw.Book('FileName.xlsx')  # connect to a file that is open or in the current working directory
# wb = xw.Book(r'C:\path\to\file.xlsx')  # on Windows: use raw strings to escape backslashes

app = xw.App()
wb = xw.Book(r'申万财务模型5.0.4中英文版-20200320.xlsm')

sheet = wb.sheets['公司说明']

print(sheet.range('E4').value)
sheet.range('E4').value = '300750'
print(sheet.range('E4').value)

print(sheet.range('E10').value)
print(sheet.range('E10').formula)

print(wb.sheets['财务分析'].range('G46').value)

wb.close()
app.quit()