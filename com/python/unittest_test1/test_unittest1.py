"""
unitest Python 自带单元测试
the first unitest at 202102121759
没加类方法装饰器 @classmethod执行结果报错
"""
import unittest

class TestStringMethods(unittest.TestCase):
    #在测试用例之前执行
    def setUp(self) -> None:
        print("setup")
    #在测试用例之后执行
    def tearDown(self) -> None:
        print("teardown")
    #类方法，加上@classmethod装饰器，在测试类调用之前调用
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
    #类方法，加上@classmethod装饰器，在测试类调用之后调用
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def test_abc(self):
        print("test_abc")

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_issupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
