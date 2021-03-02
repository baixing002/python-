"""
test_search 模块里有两个类 ：TestSearch1 & TestSearch2
"""
import unittest


class Search:
    #被测试方法
    def search_func(self):
        print("search")
        return True
#继承unittest里的TestCase类
class TestSearch1(unittest.TestCase):

    #在测试类TestSearch调用之前，定义一个 (加@classmethod装饰器)类方法：setUpClass，传参（cls）
    @classmethod
    def setUpClass(cls) -> None:
        #实例化Search()类，后面就可以用self. 实例参数去调用
        print("setup class_1")
        cls.search = Search()
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class_1")

    def setUp(self) -> None:
        print("set up")
        self.search = Search()
    def tearDown(self) -> None:
        print("tear down")
    def test_search1(self):
        print("test search1")
        # search = Search()
        assert True == self.search.search_func()
    def test_search2(self):
        print("test search2")
        # search = Search()
        assert True == self.search.search_func()

    def test_search3(self):
        print("test search3")
        # search = Search()
        assert True == self.search.search_func()
class TestSearch2(unittest.TestCase):

    #在测试类TestSearch调用之前，定义一个 (加@classmethod装饰器)类方法：setUpClass，传参（cls）
    @classmethod
    def setUpClass(cls) -> None:
        #实例化Search()类，后面就可以用self. 实例参数去调用
        print("setup class_2")
        cls.search = Search()
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class_2")

    def setUp(self) -> None:
        print("set up")
        self.search = Search()
    def tearDown(self) -> None:
        print("tear down")
    def test_search1(self):
        print("test search1")
        # search = Search()
        assert True == self.search.search_func()
    def test_search2(self):
        print("test search2")
        # search = Search()
        assert True == self.search.search_func()

    def test_search3(self):
        print("test search3")
        # search = Search()
        assert True == self.search.search_func()
    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"判断 1 == 1")
    #命名规范case名字前面加 test 关键字表示一个测试case
    def test_notequal(self):
        print("断言表达式1==1是否相等")
        # print("断言不相等")
        # self.assertNotEqual(1,2,"判断 1 != 2")
        #判断表达式是否相等
        self.assertTrue(1==1,"verify 判断表达式是否相等")
if __name__ == '__main__':
    #方法一：执行当前文件所有的unittest测试用例（执行当前测试页面所有测试类用例）
    unittest.main()
    #方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行
    #创建一个测试套件，testsuite
    suite = unittest.TestSuite()
    suite.addTest(TestSearch1("test_search1"))
    suite.addTest(TestSearch1("test_search2"))
    unittest.TextTestRunner().run(suite)
    #方法三：执行某个测试类，将测试类添加到测试套间里面，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)