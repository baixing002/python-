"""
执行某个目录下面所有以test开头的py文件，执行这些文件写的所有测试用例

"""
import  unittest

from com.python.util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = 'Example用例执行报告_我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'

    test_dir = './unittest_test1'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)