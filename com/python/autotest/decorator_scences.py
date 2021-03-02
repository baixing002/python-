"""
装饰器的应用场景：
logging
"""
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__+ " was called")
        return func(*args,**kwargs)
    return with_logging
@logit
def addition_func(x):
    """Do some math."""
    return x + x
result = addition_func(4)
#addition_func was called
