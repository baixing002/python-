"""
def 函数的定义
"""
# a=2
# print(a)
def function(a,b,c):
    """
    介绍函数funcion的作用
    :param a:参数a是用来打印
    :param b:
    :param c:
    :return:
    """
    #使用tab键添加缩进
    print("这是一个函数")
    #pycharm快捷键 ctrl + d :复制一行
    print("这是一个函数a:",a)
    print("这是一个函数a:",b)
    print("这是一个函数a:",c)
#函数的调用
#定义函数只有在调用的时候，才能打印出来，如果没有外部去调用定义的函数，执行打印是打印不出来的
#函数传参的顺序：位置参数 3，2，1
function(1,2,3)
function(3,2,1)