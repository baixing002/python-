from openpyxl import Workbook

# 新建工作簿
new_wb = Workbook()
# 将新建的工作簿保存为【new_excel.xlsx】
new_wb.save('./new_excel.xlsx')