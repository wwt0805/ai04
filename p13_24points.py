# 给任意4张扑克牌，编写程序判断该四张卡牌是否可以运算得出24.
import itertools as it
import numpy as np


def get_numbers(num):
    return list(np.random.randint(1, 13 + 1, [num]))


def make(numbers, target):
    print(numbers)
    for value, exp in get_exps(numbers):  # get_exp产生的二元组的列表
        if value == target:
            print(exp)


def get_exps(numbers):  # 递归边界
    if len(numbers) == 1:
        return [(numbers[0], str(numbers[0]))]  # 返回二元组列表，值和表达式

    result = []
    total = {e for e in range(len(numbers))}  # {0， 1， 2， 3}
    for left in range(1, len(numbers)):   # 从total里取出若干个元素
        for left_ids in it.combinations(total, left):    # left_ids = {0},{1},{2}……
            right_ids = total - set(left_ids)      # right_ids就是从total取出left_ids后剩余的部分 若left_ids = {0}, 则right_ids = {1},{2},{3}

            left_numbers = [numbers[i] for i in left_ids]
            right_numbers = [numbers[i] for i in right_ids]

            for left_value, left_exp in get_exps(left_numbers):
                for right_value, right_exp in get_exps(right_numbers):
                    value = left_value + right_value
                    exp = "({} + {})".format(left_exp, right_exp)
                    result.append((value, exp))

                    value = left_value - right_value
                    exp = "({} - {})".format(left_exp, right_exp)
                    result.append((value, exp))

                    value = left_value * right_value
                    exp = "({} * {})".format(left_exp, right_exp)
                    result.append((value, exp))

                    if right_value != 0:
                        value = left_value / right_value
                        exp = "({} / {})".format(left_exp, right_exp)
                        result.append((value, exp))
    return result
                    

numbers = get_numbers(4)
make(numbers, 24)