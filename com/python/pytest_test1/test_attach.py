"""
allure.attach 可以显示图片和html,可以补充测试、步骤或测试结果
"""
import allure
import pytest
#添加一个纯文本
def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

#添加的图片没有展示出来???--一个遗留的问题
def test_attach_photo():
    allure.attach.file("E:\PythonData\com\python\pytest_test1\resource\20210220.jpg",
                  name="这是一个图片",attachment_type=allure.attachment_type.JPG)
def test_attach_photo_test():
    print("test")
    pass