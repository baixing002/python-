"""
字典
"""
#定义
dict1 ={"a":1,"b":2}
dict2 = dict(a=1,b=2)
print(type(dict1))
print(dict1)
print(type(dict2))
print(dict2)
#常用内置函数
print(dict1.keys())
print(dict1.values())
#删除键值对
print(dict1.pop("a"))
print(dict1)
#popitem(随机删除键值对)
print(dict2.popitem())
print(dict2)
#
a={}
b1 = a.fromkeys([1,2,3],"a")
b2 = a.fromkeys((1,2,3),"a")
print(b1)
print(b2)
#字典推导式
print({i:i*2 for i in range(1,3)})