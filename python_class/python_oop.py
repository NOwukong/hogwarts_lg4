# -*- coding: utf-8 -*-
# @Time     :2020/12/1 21:44
# @Author   :xiangdong
# @File     :python_oop.py

# 面向对象
class House:
    # 静态属性->类变量（类之中，方法之外）
    door = 'red'
    floor = 'black'

    # 构造函数，在类实例化的时候直接执行
    def __init__(self):
        # 在方法当中调用类变量新需要加上self.
        print(self.door)
        # 实例变量，类当中，方法当中,以“self.变量名”方式定义
        self.kitchen = 'cook'

    # 动态方法
    def sleep(self):
        # 普通变量：类当中，方法当中，前面没有 self
        bed = '席梦思'
        self.table = '桌子可以放东西'
        print(f"在房子里可以躺在{bed}上睡觉")

    def cook(self):
        print(self.kitchen)
        print(self.table)
        print("在房子里可以做饭")


# 把类实例化
# 北欧风格房子
north_house = House()
# 中式风格房子
# china_house = House()

# print(north_house.sleep())
print(north_house.sleep())
print(north_house.cook())
