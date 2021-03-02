from openpyxl import load_workbook

# 设置文件路径
file_path = './事业01部_副本.xlsx'

# 打开工作簿
wb = load_workbook(file_path)
# 打开工作表
ws = wb.active

# 将第一列的列宽调整为10
ws.column_dimensions['A'].width = 10

# 将第二列的列宽调整为25
ws.column_dimensions['B'].width = 25

# 将第三列的列宽调整为50
ws.column_dimensions['C'].width = 50

# 将第四列的列宽调整为10
ws.column_dimensions['D'].width = 10

# 将第五列的列宽调整为20
ws.column_dimensions['E'].width = 20

# 将第六列的列宽调整为15
ws.column_dimensions['F'].width = 15

# 保存
wb.save(file_path)