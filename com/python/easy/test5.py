from openpyxl import load_workbook

# 打开【公司人员名单.xlsx】工作簿
staff_wb = load_workbook('./公司人员名单.xlsx')
# 获取活动工作表
active_ws = staff_wb.active

info_list = ['S1911', '萧爵瑟', 3000, '内容']
info_tuple = ('S1912', '吴琐薇', 5000, '销售')

active_ws.append(info_list)
active_ws.append(info_tuple)

# 保存工作簿为【append_demo.xlsx】
staff_wb.save('./append_demo.xlsx')