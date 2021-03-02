"""
args 和 *kwargs 的用法
我观察到，大部分新的Python程序员都需要花上大量时间理解清楚 *args 和**kwargs这两个魔法变量。那么它们到底是什么?
首先让我告诉你, 其实并不是必须写成*args 和**kwargs。
只有变量前面的 *(星号)才是必须的. 你也可以写成*var 和**vars. 而写成*args 和**kwargs只是一个通俗的命名约定。 那就让我们先看一下*args吧。

"""
#-------------------*args的用法---------------
"""
*args 和 **kwargs 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。
这里的不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。 
*args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
"""
print("--------------*args的用法--------------------")
def test_var_args(f_arg,*argv):
    print("first normal arg:",f_arg)
    for arg in argv:
        print("another arg through *argv")
test_var_args('yasoob','python','eggs','test')
#*args ---代表传递的所有参数
def test_var_args2(*b):
    for i in b:
        print(i)
test_var_args2('a','b','c','d')
print("--------------**kwargs的用法------------------")
"""
**kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs
"""
def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0}=={1}".format(key,value))
greet_me(name = "hufeng")

print("-----------使用 args 和 *kwargs 来调用函数-----------------")
"""
现在你可以看出我们怎样在一个函数里, 处理了一个键值对参数了。
这就是**kwargs的基础, 而且你可以看出它有多么管用。 接下来让我们谈谈，你怎样使用*args 和 **kwargs来调用一个参数为列表或者字典的函数。
"""
#使用 args 和 *kwargs 来调用函数
def test_args_kwargs3(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)
"""
你可以使用*args或**kwargs来给这个小函数传递参数。 下面是怎样做：
"""
#首先使用*args
args = ("two",3,5)
test_args_kwargs3(*args)

#现在使用 **kwargs:
kwargs = {"arg3":3,"arg2":"two","arg1":5}
test_args_kwargs3(**kwargs)

"""
标准参数与*args、**kwargs在使用时的顺序
那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
some_func(fargs, *args, **kwargs)
"""
# some_func(fargs, *args, **kwargs)
"""
啥时候使用它们
这还真的要看你的需求而定。
最常见的用例是在写函数装饰器的时候（会在另一章里讨论）。
此外它也可以用来做猴子补丁(monkey patching)。猴子补丁的意思是在程序运行时(runtime)修改某些代码。 
打个比方，你有一个类，里面有个叫get_info的函数会调用一个API并返回相应的数据。如果我们想测试它，
可以把API调用替换成一些测试数据。例如
"""
# import someclass
# # #
# # # def get_info(self, *args):
# # #     return "Test data"
# # #
# # # someclass.get_info = get_info