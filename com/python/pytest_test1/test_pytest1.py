"""
pytest 测试框架
"""
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

