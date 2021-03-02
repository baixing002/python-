"""
带参数的装饰器
decorato with parameters
来想想这个问题，难道@wraps不也是个装饰器吗？但是，
它接收一个参数，就像任何普通的函数能做的那样。
那么，为什么我们不也那样做呢？ 这是因为，当你使用@my_decorator语法时，
你是在应用一个以单个函数作为参数的一个包裹函数。
记住，Python里每个东西都是一个对象，而且这包括函数！记住了这些，我们可以编写一下能返回一个包裹函数的函数
"""
from functools import wraps
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__+ "was called"
            print(log_string)
            #打开logfile,并写入内容
            with open(logfile,'a') as opened_file:
                #将日志打到指定的logfile文件中
                opened_file.write(log_string + '\n')
            return func(*args,**kwargs)
        return wrapped_function
    return logging_decorator
@logit()
def myfunc1():
    pass
myfunc1()
#output:myfunc1was called
#一个叫做 out.log 的文件被创建出来，里面写入的内容就是打印出来的内容
@logit(logfile='func2.log')
def myfunc2():
    pass
myfunc2()
#myfunc2was called
#一个叫做func2.log 的文件被创建出来，里面写入的内容就是打印出来的内容