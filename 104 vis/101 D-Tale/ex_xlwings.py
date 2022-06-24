import xlwings as xw

app = xw.App(visible=True, add_book=False)
app.properties(display_alerts=False)
wb = xw.Book('CN.xlsx')

sheet = wb.sheets['Sheet1']

sheet.range('E1').value = '这是Python写到单元格里的一行字'
print("E1单元格现在的内容是：", sheet.range('E1').value)

sheet.range('F1').formula = '=E1'
print("F1单元格现在的公式是：", sheet.range('F1').formula)
print("F1单元格现在的内容是：", sheet.range('F1').value)

input("请按回车键继续...")
wb.close()
app.quit()