"""
fixture : 用法
用fixture 实现不同的测试用例准备
--autouse  作用域为 所有的测试方法
--fixture 和 set up 同时存在的话，fixture的优先级更高（一般不会这样同时用）
"""

import pytest

#方法一：
#加上pytest的fixture装饰器，变成fixture()方法
@pytest.fixture()
def login():
    print("用户登陆")
    print("获取 token")
    username = "tom"
    password = "123456"
    token = "token456jkl"
    #yield 关键字可以激活 fixture 的 teardown 功能
    ##用yield 生成用户登录的信息，相当于return,返回数据可以直接跟在yield后面
    yield [username,password,token] ## 用yield 生成用户登录的信息
    print("注销操作")
def setup():
    print("setup---method")
"""在测试用例中传入 fixture 方法名实现调用登陆"""
#需要提前登陆
def test_case1(login):
    #获取fixture方法的返回值，直接调用fixture方法名
     print("用户信息为：{}".format(login))
     print("测试用例1")


def test_case2(connectDB):
    print("测试用例2")

"""在测试用例中传入 fixture 方法名实现调用登陆"""
#需要提前登陆
def test_case3():
    print("测试用例3")

#方法二：（优点--可以不用向方法里面传参）
#使用装饰器的方法，实现用户先登陆操作,装饰器传入的参数为字符串
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")

