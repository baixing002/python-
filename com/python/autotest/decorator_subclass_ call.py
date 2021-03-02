"""
调用子类装饰器
call_subclass_decorator
"""
from com.python.autotest.decorator_subclass import email_logit

class callDecorator:
    @email_logit()
    def func_call(x):
        """hi,decorator,come on!"""
        return x

call_decorator = callDecorator()
call_decorator.func_call()

# @email_logit()
# def func_call():
#     """hi,decorator,come on!"""
#     pass
# func_call()