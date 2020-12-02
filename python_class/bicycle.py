# -*- coding: utf-8 -*-
# @Time     :2020/12/1 22:36
# @Author   :xiangdong
# @File     :bicycle.py

# 自行车类
class Bicycle():
    def run(self, km):
        print(f'一共用脚骑了{km}公里，累死了')


# 电动自行车类
# 继承：将父类名称放在类名的括号内
class EBicycle(Bicycle):
    # 属性可以传参定义，可以放在构造函数中,传入初始电量value值
    def __init__(self, value):
        self.value = value

    # 充电方法
    def fill_charge(self, vol):
        # 充电后的电量 = 本身电量 + 充电电量
        self.value += vol
        print(f'充了{vol}度电，当前还剩{self.value}度电')

    # 骑行方法
    """
    run（km）方法用于骑行，每骑行10km消耗1度电
    当电量消耗尽时调用Bicycle的run方法骑行，通
    过传入的骑行里程数，显示骑行结果
    """
    # 子类定义的方法名与父类的相同时 等于重写该方法，方法以子类重写定义的为准
    def run(self, km):
        # 1. 获取目前电量所能七星的最大里程数
        power_km = self.value * 10

        if power_km >= km:
            print(f'我使用电瓶电量骑行了{km}公里')
        else:
            # 电量不够了，在电量用完后用脚骑行,定义一个剩余公里 ride_km（脚骑）
            ride_km = km - power_km
            print(f'我用电瓶电量骑行了{power_km}公里，还用脚骑了{ride_km}公里')
            # 实例化嵌套，在实例化之前也可以先生成一个实例化（非继承父类的方法）
            # bike = Bicycle()
            # bike.run(km - power_km)

            # 继承父类调用
            super().run(km-power_km)


# 调用类生成实例bike
# bike = Bicycle()
# 调用实例化后的 run 方法 (需传入方法参数km值)
# bike.run(20)
# 调用类生成实例 ebike
ebike = EBicycle(10)
# ebike.fill_charge(5)
ebike.run(150)
