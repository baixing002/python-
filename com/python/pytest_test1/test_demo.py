"""
Python 数据驱动
"""
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("yaml文件里的内容是：",env)
            print("测试环境的IP是_双引：",env["test"])
            print("测试环境的IP是_单引：",env['test'])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的IP是:",env["dev"])
    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))