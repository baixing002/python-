"""
fixture的作用域
--fixture 只能放在方法上面，不能放在其他的上面
--function 作用域是在方法上
--class    作用域是在类上
--module   作用域是在文件模块上
"""
import pytest


# @pytest.fixture(scope="module")
# def connectDB():
#     print("连接数据库的操作")
#     yield
#     print("断开数据库的连接")


class TestDemo:

    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")

class TestDemo1:

    def test_c(self,connectDB):
        print("测试用例c")

    def test_d(self,connectDB):
        print("测试用例d")