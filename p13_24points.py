import numpy as np


def get_numbers(num):
    return list(np.random.randint(1, 13 + 1, [num]))


def make(numbers, target):
    print(numbers)
    for value, exp in get_exps(numbers):
        if value == target:
            print(exp)


def get_exps(numbers):
    if len(numbers) == 1:
        return [(numbers[0], str(numbers[0]))]

    result = []
    total = {e for e in range(len(numbers))}
    for left in range(1, len(numbers)):
        for left_ids in comb(total, left):
            right_ids = total - left_ids

            left_numbers = [numbers[i] for i in left_ids]
            right_numbers = [numbers[i] for i in right_ids]

            for left_value, left_exp in get_exps(left_numbers):
                for right_value, right_exp in get_exps(right_numbers):
                    value = left_value + right_value
                    exp = "({} + {})".format(left_exp, right_exp)
                    result.append(value, exp)

                    value = left_value - right_value
                    exp = "({} - {})".format(left_exp, right_exp)
                    result.append(value, exp)

                    value = left_value * right_value
                    exp = "({} * {})".format(left_exp, right_exp)
                    result.append(value, exp)

                    value = left_value / right_value
                    exp = "({} / {})".format(left_exp, right_exp)
                    result.append(value, exp)
                    

numbers = get_numbers(4)
make(numbers, 24)