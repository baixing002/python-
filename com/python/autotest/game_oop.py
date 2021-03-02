"""
一个回合制游戏，每个角色都有 hp 和 power ，hp 代表血量，pow代表攻击力
"""
from com.python.autotest.python_log_decorator import log_decorator


class Game:
    #构造方法，初始化属性
    def __init__(self,my_hp,my_power,enemy_hp,enemy_power):
        #初始化属性
        self.my_hp = my_hp
        self.my_power = my_power
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power
        #定义私有属性
        self.__secret = "secret"

    #对打的方法
    @log_decorator
    def fight(self):
        while True:
            #计算我剩余的血量
            self.my_hp = self.my_hp - self.enemy_power
            #计算敌人的剩余血量
            self.enemy_hp -= self.my_power
            print("--------游戏开始--------------")
            print(f"我的血量：{self.my_hp} VS 敌人的血量：{self.enemy_hp}")
            #在方法中调用方法
            # self.rest(200)
            # self.rest(2000)
            #胜负判断
            if self.my_hp <= 0:
                print("--------游戏结束------------")
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("--------游戏结束------------")
                print("我赢了")
                break
    #定义休息方法
    def rest(self,time_num):
        self.__private_method1()
        # print(f"调用私有方法{self.__private_method()}")
        print(f"太累了，休息 {time_num} 分钟")
    #定义私有方法
    def __private_method1(self):
        print("这是一个私有方法 ")
        #私有方法可以拿到私有变量
        print(self.__secret)
if __name__ == '__main__':
    #实例化
    game = Game(1000,999,2000,888)
    game.fight()
    # game.rest(666999)
    # game.__private_method1()
    #调用属性
    # print(game.my_power)
    """
    私有变量不能通过对象去调用
    """
    #私有变量不能通过对象去调用
    # print(game.__secret)
    """
    私有方法不能通过对象去调用
    """
    # game.__private_method()