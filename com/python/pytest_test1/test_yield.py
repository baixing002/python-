"""
yield
生成器
"""

def provider():
    #循环读取数据
    for i in range(10):
        #一次生成一行数据
        print("开始操作")
        yield i
        print("结束操作")

#普通函数调用
p = provider()
# print(p)
#生成器用next()方法调用
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

