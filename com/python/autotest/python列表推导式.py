"""
列表推导式
如果我们想生成一个平方列表，比如[1,4,9...],使用for循环应该 怎么写，，使用列表生成式又该怎样写？
"""
#range(1,4) 左闭右开--右边取不到
list_1=[]
for i in range(1,4):
    list_1.append(i*i)
print(list_1)

list_2=[i*i for i in range(1,4)]
print(list_2)

list_3=[]
for i in range(1,4):
    if i !=1:
        list_3.append(i**2)
print(list_3)
list_3=[i**2 for i in range(1,4) if i !=1]
print(list_3)

list_4=[]
for i in range(1,4):
    for j in range(1,4):
        list_4.append(i*j)
print(list_4)
list_4=[i*j for i in range(1,4) for j in range(1,4)]
print(list_4)