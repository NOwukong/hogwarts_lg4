# -*- coding: utf-8 -*-
# @Time     :2020/11/30 20:50
# @Author   :xiangdong
# @File     :game_round_more.py

# 定义fight函数实现游戏逻辑
import random


def fight(enemy_hp, enemy_power):
    # 定义四个变量存放数据
    my_hp = 1000
    my_power = 200

    # 打印敌人血量和攻击力
    print(f"敌人的血量为{enemy_hp},攻击力为{enemy_power}")

    # enemy_hp = 1000
    # enemy_power = 199

    # 加循环函数，使游戏进行多轮
    while True:
        # 定义最终血量计算方式
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # print('我的血量：%d' % my_hp)
        # print('敌人的血量%d：' % enemy_hp)

        # 判断最终血量谁大于0 为赢者
        if my_hp <= 0:
            print(f'我的剩余血量{my_hp}')
            print(f'敌人的剩余血量为{enemy_hp}')
            print('我输了')
            # 满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print(f'我的剩余血量{my_hp}')
            print(f'敌人的剩余血量为{enemy_hp}')
            print('我赢了')
            # 满足条件跳出循环
            break


if __name__ == '__main__':
    # 利用列表推倒式生产hp
    hp = [x for x in range(990, 1010)]
    # print(hp)
    # print(type(hp))
    # 随机生产敌人血量值
    enemy_hp = random.choice(hp)
    # print(enemy_hp)

    # 敌人的攻击了用randint方法生产一个随机整数
    enemy_power = random.randint(190, 210)
    # print(enemy_power)

    # 调用函数，传入随机定义的敌人参数
    fight(enemy_hp, enemy_power)