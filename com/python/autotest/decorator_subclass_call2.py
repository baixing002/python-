"""
子类装饰器的调用

"""
from com.python.autotest.decorator_subclass import email_logit


@email_logit()
def my_func8():
    "子类装饰器的调用"
    pass

my_func8()