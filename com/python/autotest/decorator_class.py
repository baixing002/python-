"""
装饰器类
decorator class
"""
from functools import wraps

class logit(object):
    def __init__(self,logfile='out.log'):
        self.logfile = logfile
    def __call__(self,func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ + "我是父类装饰器类里的was called"
            print(log_string)
            #打开logfile并写入
            with open(self.logfile,'a') as opened_file:
                #将日志打到指定的文件
                opened_file.write(log_string + '\n')
            #现在，发送一个通知
            self.notify()
            return func(*args,**kwargs)
        return wrapped_function
    def notify(self):
        #loggit只打日志，不做别的
        pass

# @logit()
# def myfunc6():
#     pass
# myfunc6()
