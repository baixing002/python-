"""
python的输入与输出--字面量插值
%s：字符串
%d：数据/数字类型--十进制的整数
%f :引用浮点数
%.2f:保存小数点后两位
format
"""
#%
age=3
name = 'hufeng'
list1 = [1,3,4]
dict1 = {'name':'胡枫','gender':'male'}
namelist=['胡枫','胡金秋','胡翔宇']
print('my name is %s,my age is %d,num is %f'%(name,age,3.1415))
print('my name is %s,my age is %d,num is %.2f'%(name,age,3.1415))
#format
print('my name is {},my age is {}'.format(name,age))
print('my name is {0},my age is {1}'.format(name,age))
print('my name is {0},my age is {1},{0}{1}{1}'.format(name,age))
#字典
print('my list is {},my dict is {}'.format(list1,dict1))
print('my list is {0},my dict is {1}'.format(list1,dict1))
#*x  --解剖列表
print('my name is:{}、{} and {}'.format(*namelist))
#**X --字典的解包
print('my name is {name},my gender is {gender}'.format(**dict1))


