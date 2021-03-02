"""
定义一个后羿的类
后羿继承了 Game 的hp和power ,并对了护甲属性

"""
# from game_oop import Game
# 继承Game类，在括号里写上要继承的类的名字
from com.python.autotest.game_oop import Game
from com.python.autotest.python_log_decorator import log_decorator


class HouYi(Game):
    # 重写了父类的构造方法
    def __init__(self,my_hp,my_power,enemy_hp,enemy_power):
        self.defense = 100
        # 使用super()继承父类的构造方法
        super().__init__(my_hp,my_power,enemy_hp,enemy_power)
    @log_decorator
    def fight(self):
        # 重写my_hp 的计算方式、
        while True:
            # 计算我剩余的血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            # 计算敌人的剩余血量
            self.enemy_hp -= self.my_power
            print("--------游戏开始--------------")
            print(f"我的血量：{self.my_hp} VS 敌人的血量：{self.enemy_hp}")
            #使用super()调用父类的rest()方法
            super().rest(6)
            #使用self. 调用rest()方法
            #我继承了父类，在方法中调用方法，完全可以
            self.rest(100)
            self.rest("一分钟")
            # 胜负判断
            if self.my_hp <= 0:
                print("--------游戏结束------------")
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("--------游戏结束------------")
                print("我赢了")
                break
    def rest(self,wait_time):
        self.__private_method1()
        print(f"我是子类重写父类的rest方法,想休息{wait_time}分钟")
        print("我重写了父类的rest方法")
    def __private_method1(self):
        print("test继承父类的私有方法")

if __name__ == '__main__':
    #实例化（创建对象）对构造方法进行传参
    houyi = HouYi(1000,999,2000,888)
    # 子类的对象可以直接调用父类的属性和方法
    # print(houyi.my_power)
    houyi.fight()
    # houyi.rest(6)
