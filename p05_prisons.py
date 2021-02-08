'''
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 4:14 下午
@Site    : 
@File    : p05_prisons.py
@Software: PyCharm
'''
import random

def solve_prisons(num):
    counter = num - 1
    turn_ons = [False] * (num - 1)  # 状态列表，用于记录状态
    lamp = False
    count = 0

    while True:
        lucky = random.randint(0, num - 1)
        lamp, count = get_free(lucky, counter, turn_ons, lamp, count)
        if count == num - 1:
            break

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


solve_prisons(4)