"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 11:49 上午
@Site    :
@File    : p03_pokes.py
@Software: PyCharm
"""


class CalculatePoke:
    def __init__(self, num):
        self.num = num

    def get_pokes(self):
        result = [self.num]
        p = self.num - 1
        while p > 0:
            self.insert(p, result)
            p -= 1
        return result

    @staticmethod
    def insert(p, result):
        for _ in range(p):
            last = result[-1]
            del result[-1]
            result.insert(0, last)
        result.insert(0, p)


if __name__ == "__main__":
    print(CalculatePoke(20).get_pokes())
