"""
装饰器子类的继承

"""
from com.python.autotest.decorator_class import logit


class email_logit(logit):
    """一个logit的实现版本，可以在函数调用时发送email给管理员"""
    def __init__(self,email='admin@myproject.com',*args,**kwargs):
        self.email = email
        super(email_logit,self).__init__(*args,**kwargs)
    def notify(self):
        #发送一封email到self.email
        #这里就不做实现了
        pass

