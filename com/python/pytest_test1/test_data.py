"""
pytest--参数化  ----string,tuple,list

"""
import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data_yaml.yaml")))
    def test_data(self,a,b):
        print(a+b)
