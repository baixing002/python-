"""
conftest 公共文件，放在测试用例的同一个包下面
--session 多个文件一起执行
思路二: 把登录方法 放到conftest 公共配置文件里面
"""
import pytest

#加上fixture装饰器变成fixture方法
from com.python.test_code.calc import Calculator#从最开始的包路径开始导入  --com/python/test_code/calc.py


@pytest.fixture(scope="module")
def connectDB():
    print("连接数据库的操作")
    yield
    print("断开数据库的连接")

#fixture 方法get_calc() 的作用域是class
@pytest.fixture(scope='class')
def get_calc():
    print("获取计算器的实例")
    calc = Calculator()
    return calc