"""
test_ordering
pytest 是按照用例的执行顺序。unitest 是按照 用例名称的ASC码顺序执行
"""

import pytest
from time import sleep

@pytest.mark.run(order=2)
def test_1():
    sleep(1)
    assert True

@pytest.mark.run(order=3)
def test_2():
    sleep(1)
    assert True

@pytest.mark.run(order=1)
def test_3():
    sleep(1)
    assert True
