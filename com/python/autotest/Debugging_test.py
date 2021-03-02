"""
Debugging  调试用法
"""
"""
从命令行运行
你可以在命令行使用python debugger 运行一个脚本，举个例子
"""
# python -m pdb my_script.py

"""
从脚本内部运行
同时，你也可以在脚本内部设置断点，
这样就可以在某些特定点查看变量信息和各种执行时信息了。
这里将使用pdb.set_trace()方法来实现。
举个例子
"""
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't hava time"
print(make_bread())

"""
c: 继续执行
w: 显示当前正在执行的代码行的上下文信息
a: 打印当前函数的参数列表
s: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）
"""