"""
python实战
class 类名：
    多个类属性
    多个类方法
"""
#类名，驼峰命名规则（首字母大写）
class House:
    #静态属性，类变量，在类之中，方法之外定义
    door = "red"
    floor = "white"
    #动态方法
    def sleep(self):
        #方法变量（普通变量--方法之中，并且前面没有self.开头）
        bed = "席梦思"
        print(f"在房子里可以躺在{bed}上睡觉")
    def cook(self):
        print("在房子里可以做饭吃")
if __name__ == '__main__':
    #实例化  --> 变量名 = 类()
    north_house = House()
    china_house = House()
    #通过实例对象调用类中的属性和方法
    print(north_house.sleep())
    print(north_house.door)
    #通过类调用自己的属性和方法
    print(House.door)
    # print(House.cook())
    """
    通过类修改属性的值
    """
    House.door = "hufeng's door"
    print(north_house.door)
    print(House.door)
    """
    通过实例修改属性的值（只会修改【实例】的属性，不会修改【类】的属性）
    """
    north_house.door = "hujinqiu's door"
    print("-------实例修改属性的值调用的结果-----------")
    print(north_house.door)
    print(House.door)
    print(china_house.door)




