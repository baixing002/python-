"""
自定义sub_demo
test_sub_demo1
本模块中的fixture方法：connectDB
"""
import pytest

@pytest.fixture()
def connectDB():
    print("连接本模块test_sub_demo1_connectDB")
    yield
    print("断开本模块test_sub_demo1_connectDB")

def test_a(connectDB):
    print("sub_demo test_a")

class TestA:
    def test_b(self):
        print("sub_demo test_b")