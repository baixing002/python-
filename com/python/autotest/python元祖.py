"""
元组
"""
#元祖的定义
tuple1 = (1,2,3)
tuple2 = 1,2,3
print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
#元组的不可变性
list_1 =[1,2,3]
list_1[0]="a"
print(list_1)
#会报错
# tuple1[0]="a"
# print(tuple1)
#元组的可嵌套性
a =[1,2,3]
tuple3=(1,2,a)
print(id(tuple3[2]))
tuple3[2][0]="b"
print(id(tuple3[2]))
print(tuple3)
#元组的内置函数
c=(1,2,3,"a","a")
print(c.count("a"))
print(c.index(3))
print(c.index("a"))
