"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/14 11:27 上午
@Site    : 
@File    : p08_rabbits.py
@Software: PyCharm
"""


class Calculate:
    def __init__(self, months):
        self.months = months

    def get_rabbits(self):
        if self.months <= 2:
            return 1
        return Calculate(self.months - 1).get_rabbits() + Calculate(self.months - 2).get_rabbits()


def get_rabbits(months, store):
    if store is None:
        store = {}
    if months <= 2:
        return 1
    if months in store:
        return store[months]
    result = get_rabbits(months - 1, store) + get_rabbits(months - 1, store)
    store[months] = result
    return result

if __name__ == "__main__":
    for months in range(1, 50 + 1):
        print(months, Calculate(months).get_rabbits())
