"""
python实战
class 类名：
    多个类属性
    多个类方法
self 指代类的实例
def 函数()在类的外面def fuction() ，括号里没有参数self
def 方法（self） 在类的里面
"""
#类名，驼峰命名规则（首字母大写）
class House:
    #静态属性，类变量，在类之中，方法之外定义
    door = "red"
    floor = "white"
    """
    构造方法，在类实例化的时候自动调用（在创建对象的时候，默认调用构造方法）
    """
    def __init__(self):
        # self.door -- 加上self. 变成实例变量
        print(self.door)
        #定义实例变量--类之中，方法之内，以self.变量名 方式定义
        #实例变量的作用域是整个类中的所有方法（都可以调用）
        self.kitchen = "cook"
    #动态方法
    def sleep(self):
        #方法变量（普通变量--方法之中，并且前面没有self.开头,作用域是本方法之内）
        bed = "席梦思"
        #实例变量（作用域是整个类中）
        self.quilt = "Silk quilt"
        print(f"在房子里可以躺在{bed}上,盖上{self.quilt}睡觉")
    def cook(self):
        print(self.quilt)
        print(f"在房子里可以做饭吃,也可以躺在软绵绵的{self.quilt}上")

if __name__ == '__main__':
    #创建对象（实例化）的时候默认调用构造方法
    # north_house = House()
    china_house = House()
    china_house.sleep()
    china_house.cook()





