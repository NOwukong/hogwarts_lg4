# -*- coding: utf-8 -*-
# @Time     :2020/12/2 23:30
# @Author   :xiangdong
# @File     :game_oop.py

class Game:
    # 定义四个变量存放数据
    def __init__(self, my_hp, enemy_power):
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_power
        self.enemy_power = 200

    def fight(self):
        # 加循环函数，使游戏进行多轮
        while True:
            # 定义最终血量计算方式
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print('我的血量：%d' % self.my_hp + ', 敌人的血量：%d' % self.enemy_hp + ' ;')

            # 判断最终血量谁大于0 为赢者
            if self.my_hp <= 0:
                print(f'我的剩余血量:{self.my_hp}')
                print(f'敌人的剩余血量为:{self.enemy_hp}')
                print('我输了 T-T')
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                print(f'我的剩余血量:{self.my_hp}')
                print(f'敌人的剩余血量为:{self.enemy_hp}')
                print('我赢了 ^_^')
                # 满足条件跳出循环
                break

    def rest(self, time_num):
        print(f'太累了，休息{time_num}分钟')


# 定义一个 继承Game 父类 的新子类 后羿 游戏
class HouYi(Game):
    def __init__(self, my_hp, enemy_hp):
        self.defense = 100
        super().__init__(my_hp, enemy_hp)

    # 改造 fight 方法 增加护甲值，重写计算战斗计算方法
    def fight(self):
        while True:
            # 定义最终血量计算方式
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print('我的血量：%d' % self.my_hp + ', 敌人的血量：%d' % self.enemy_hp + ' ;')

            # 判断最终血量谁大于0 为赢者
            if self.my_hp <= 0:
                print(f'我的剩余血量:{self.my_hp}')
                print(f'敌人的剩余血量为:{self.enemy_hp}')
                print('我输了 T-T')
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                print(f'我的剩余血量:{self.my_hp}')
                print(f'敌人的剩余血量为:{self.enemy_hp}')
                print('我赢了 ^_^')
                # 满足条件跳出循环
                break


if __name__ == '__main__':
    game = Game(1000, 1500)
    game.fight()
    houyi = HouYi(1000, 1500)
    houyi.fight()
    houyi.rest(5)