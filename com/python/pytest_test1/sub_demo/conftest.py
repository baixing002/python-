"""
sub_demo 下自定义conftest文件，属于自己定义的，不想用公共的conftest文件的时候
--新建一个子包，在子包下面建一个conftest文件用于自己的测试case用
--conftest
"""
import pytest

#fixture不指定作用域，默认是fuction级别
@pytest.fixture()
def connectDB():
    print("连接sub_demo下面的connect_DB")
    yield
    print("断开sub_demo下面的connet_DB")