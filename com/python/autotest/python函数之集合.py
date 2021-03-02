#集合的定义
a ={1}
#定义空集合
b =set()
#用len()函数查看集合的长度
print(len(b))
print(type(a))
print(type(b))
#集合的内置函数
c = {1,2,3}
b = {1,4,5}
#union函数（取并集）
print(c.union(b))
#交集
print(c.intersection(b))
#叉集
print(c.difference(b))
#集合添加元素
c.add("a")
print(c)
print({ i for i in "aaabbbcccddddeeefffggg"}) 
#集合的去重
d = "aaabbccddeeefffgghhiiijjjkkk"
print(set(d))