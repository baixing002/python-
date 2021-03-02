"""
test_calc_new

"""
import pytest
import yaml
import allure


with open("./datas/calc.yaml") as f:
    datas_f = yaml.safe_load(f)
    print("f文件里的内容为：",datas_f)
    datas = datas_f['add']
    print("datas参数为：",datas)
    add_datas = datas['datas']
    print("add_datas参数为:",add_datas)
    myid = datas['myid']
    print("myid参数为：",myid)

#每一个参数的用例名字ids = myid 取自myid
@pytest.fixture(params=add_datas,ids=myid)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")

# """
# 文件名以【test_*】开头，类名以【Test*】开头，方法名以【test_*】开头
# 注意：测试类里一定不要加__init__()方法
# """
@allure.feature("测试计算器")
class TestCalc:
    """
    优化点：
    1. 把setup 和 teardown 换成了fixture 方法 get_calc
    2. 把get_calc 方法放到conftest 中
    3. 把参数化换为了 fixture 参数化方式
    4. 测试用例中的数据需要通过get_datas获取
    5. get_datas 返回了一个列表[0.1,0.2,0.3] 分别代表了 a, b, expert

    """
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self, get_calc, get_datas):
        """
        实例化计算器 ： self.calc = Calculator()
        定义result变量接收add方法的返回值
        调用相加方法
        """
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_datas[0],get_datas[1])
            #如果result是浮点类型的参数，就是保留两位小数
            if isinstance(result, float): # float
                result = round(result, 2)
            #得到相加结果之后写断言
            assert result == get_datas[2]