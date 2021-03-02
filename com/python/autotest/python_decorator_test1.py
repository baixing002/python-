"""
python 三大神器之装饰器（熟练运用之必备进阶）
decorator，是用于扩展（增加）原来函数功能的一种函数，它的特殊之处在于：其返回值也是一个函数。就是一个返回函数的高阶函数。
如果没有装饰器，若想给一个函数增加新功能，最直接的办法是 修改（篡改）原函数代码。很多情况下，不允许或不便修改原函数代码，装饰器 应运而生。
"""

a_string = "this is a global variable"
def func1():
    """
    在函数内部给全局变量赋值
    :return:
    """
    a_string = "在函数内部给全局变量赋值"
    print(locals())
func1()
#全局变量的值并未改变
print(a_string)

def func2():
    """
    variable lifetime:变量生存周期
    值得注意的是，变量不仅生存在一个命名空间内，它还有自己的生存周期
    :return:
    """
    x = 1
func2()
# print(x) #-----NameError: name 'x' is not defined
"""
print(x) 引发的ERROR 不仅因为作用域规则导致的（尽管这是抛出了NameError的原因）
还因为与python以及其他编程语言中函数调用实现机制有关，在上述这个位置，这个执行时间点
并没有【有效的语法】能够获取到变量X的值，因为它压根不存在，即 函数 func2()的命名空间
随着函数调用开始而开始，结束而销毁
"""

def func3(x):
    """
    function parameters(函数参数)
    python允许向函数传递parameter,parameter会变成 局部变量存在于函数内部
    :return:
    """
    print(locals())
func3(1)
"""
{'x': 1}
"""

def func3_1(a, b=0):
    """
    在python中有很多方式来定义、传递参数
    函数的参数可以是必须的位置参数，或可选的命名，默认参数
    :param x:
    :return:
    """
    return a - b
print(func3_1(3, 1))
print(func3_1(3))
#func3_1()----TypeError: func3_1() missing 1 required positional argument: 'a'
print(func3_1(b=1, a=5))
"""
func3_1()--函数有一个位置参数a，一个命名参数b(默认参数)
func3_1(3, 1)--通过位置传参（3,1）覆盖默认参数
func3_1(3)--在函数调用时，可以忽略命名参数（默认参数），如若命名参数没有接收到任何值，pyton会自动使用声明的默认值（b=0）
func3_1()-- 因为忽略了位置参数，引发报错： func3_1() 缺失了一个位置参数 ：'a'
func3_1(b=1, a=5)--python支持函数调用时的命名参数（命名实参），因为有名称标记，可以忽略传递的位置顺序
"""


