# -*- coding: utf-8 -*-
# @Time     :2020/11/30 20:39
# @Author   :xiangdong
# @File     :game_round1.py

# 定义fight函数实现游戏逻辑
def fight():
    # 定义四个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
    if my_final_hp > enemy_final_hp:
        print("我赢了")
    # elif my_final_hp < enemy_final_hp:
    #     print("我输了")
    else:
        print("我输了")


fight()
