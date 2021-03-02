"""
selenium web UI 自动化测试验证
feature（）--测试case的功能描述
allure.step（）--一个一个的操作步骤名称
"""
import allure
import pytest

from selenium import  webdriver
import time

#放到测试用例的管理地址
@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):

    with allure.step("打开百度网页"):
        # driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()
    with allure.step("输入搜索词{}".format(test_data1)):
        #输入搜索词
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        #点击搜索
        driver.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./result/c.png")
        #保存的图片放到测试用例里
        allure.attach.file("./result/c.png",attachment_type=allure.attachment_type.PNG)
        #添加html文本--首页
        allure.attach('<head></head><body>首页</body>','Attach with HTML type',allure.attachment_type.HTML)
    with allure.step("关闭浏览器"):
        driver.quit()
