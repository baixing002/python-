"""
计算器 calc
"""
import pytest
import yaml
from com.python.test_code.calc import Calculator #从最开始的包路径开始导入  --com/python/test_code/calc.py

def test_a():
    print("测试用例a")

def func():
    print("普通函数")

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)
# """
# 文件名以【test_*】开头，类名以【Test*】开头，方法名以【test_*】开头
# 注意：测试类里一定不要加__init__()方法
# """
class TestCalc:
    # @classmethod
    def setup_class(self):
        print("开始计算")
        #实例化Calculator() 类
        self.calc = Calculator()
    # @classmethod
    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas,ids=myid
    )
    @pytest.mark.add
    def test_add(self, a, b, expect):
        """
        实例化计算器 ： self.calc = Calculator()
        定义result变量接收add方法的返回值
        调用相加方法
        :param a:
        :param b:
        :param expect:
        :return:
        """
        result = self.calc.add(a,b)
        if isinstance(result, float): # float
            result = round(result, 2)
        #得到相加结果之后写断言
        assert result == expect

    @pytest.mark.add
    def test_add1(self):
        #self.calc = Calculator()
        result = self.calc.add(0.1,0.1)
        assert result == 0.2

    @pytest.mark.add
    def test_add2(self):
        #self.calc = Calculator()
        result = self.calc.add(-1,-1)
        assert result == -2

    @pytest.mark.div
    def test_div(self):
        print("test_div")

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")












