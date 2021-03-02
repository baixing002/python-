"""
class
"""

#创建一个人类
#通过class定义一个类
class Person:
    #类变量
    name = "default"
    age = 0
    gender = 'male'
    weight = 0
    #初始化的一个构造方法（加载类的时候会默认调用类的构造方法）
    def __init__(self,name,age,gender,weight):
        #实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    #self 相当于this 指向自己本身的引用
    def set_param(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age
    #类方法
    @classmethod
    def eat(self):
        print("{}eating".format(self.name))
        print("{}learning".format(self.name))
    def play(self):
        print("{}playing".format(self.name))
    def jump(self):
        print("{}jump".format(self.name))
#所谓类的实例化，就是创建一个类的对象
#构造方法的传参（不同的实例，创建不同的类的对象）
hufeng = Person('hufeng',18,'male','57kg')
hufeng.eat()
zhangsan = Person('zhangsan',120,'male','55kg')
zhangsan.play()
hufeng.set_param("hufeng")
hufeng.set_age(28)
print(hufeng.name)
print(hufeng.age)
print("hufeng的姓名是：{}，hufeng的年龄是：{}".format(hufeng.name,hufeng.age))
print("zhangsan的姓名是：{}，zhangsan的年龄是：{}".format(zhangsan.name,zhangsan.age))
#类变量和实例变量的区别
print(Person.name)
Person.name = 'tom'
print(Person.name)
#
print(zhangsan.name)
zhangsan.name='lili'
print(zhangsan.name)
#类方法和实例方法的区别
#通过类直接访问方法
Person.eat()
#类方法不能访问实例方法，需要添加一个装饰器 @classmethod
Person.play()