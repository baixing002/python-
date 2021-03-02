"""
python函数之默认参数
默认参数在定义函数的时候使用k=v的形式定义
调用函数时，如果没有传递参数，则会使用默认参数
调用函数时，如果传递参数的话，则会使用传递的参数
"""
def function1(a=1):
    print("参数a的值为",a)
#调用函数时候，无传参使用默认参数
function1()
#调用函数的时候，传参，使用传递的参数
function1(3)

"""
python函数之关键字参数
在调用函数的时候，使用k=v的方式进行传参
在函数调用/定义中，关键字参数必须跟随在位置参数的后面
"""
def function2(b):
    print("参数b的值为",b)
def function3(c,d,e):
    print("参数C的值为：",c)
    print("参数d的值为：",d)
    print("参数e的值为：",e)
function2(b=2)
function3(c=10,d=20,e=30)
function3(e=30,d=20,c=10)
