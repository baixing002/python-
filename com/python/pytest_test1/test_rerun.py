"""
test_rerun
命令行里面的命令都可以加到 pytest.ini配置文件里
"""
import pytest
from time import sleep


def test_rerun1():
    sleep(0.5)
    assert 1 == 2


def test_rerun2():
    sleep(0.5)
    assert 2 == 2

#测试用例上加上flaky装饰器，执行重跑
@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun3():
    sleep(0.5)
    assert 3 == 2
