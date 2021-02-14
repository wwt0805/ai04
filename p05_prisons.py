"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 4:14 下午
@Site    :
@File    : p05_prisons.py
@Software: PyCharm
"""
import random


class PrisonersEscape:
    def __init__(self, num):
        self.num = num

    def solve_prisons(self):
        counter = self.num - 1
        turn_ons = [False] * (self.num - 1)  # 状态列表，用于记录状态
        lamp = False
        count = 0
        while True:
            lucky = random.randint(0, self.num - 1)
            lamp, count = self.get_free(lucky, counter, turn_ons, lamp, count)
            if count == self.num - 1:
                break

    @staticmethod
    def get_free(lucky, counter, turn_ons, lamp, count):
        if lucky == counter:
            if lamp:
                lamp = False
                count += 1
        else:  # 对于非计数员
            if not lamp and not turn_ons[lucky]:
                lamp = True
                turn_ons[lucky] = True
        print('luck={}, lamp={}, count={}, {}'.format(lucky, lamp, count, turn_ons))
        return lamp, count


if __name__ == "__main__":
    PrisonersEscape(4).solve_prisons()
