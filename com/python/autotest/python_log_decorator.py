"""
装饰器
"""
import logging

#设置基本配置
logging.basicConfig(level=logging.DEBUG)#设置日志级别一定要大写（.....）
#自定义logger
logger = logging.getLogger('log')

#func(a,b,c)

#定义装饰器
def log_decorator(func):
    """
    给传输的函数添加日志信息
    :param func: 传入的函数
    :return: 添加好了log信息的函数
    """
    def wrapper(*args,**kwargs):
        # 加上log信息
        logger.debug(f"装饰器：{log_decorator.__name__}-> 传入函数：{func.__name__ }")
        #调用传输函数对象
        return func(*args,**kwargs)
    return wrapper