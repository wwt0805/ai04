"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 2:11 下午
@Site    :
@File    : p03_pokes_seq1.py
@Software: PyCharm
"""


class CalculatePoke:
    def __init__(self, num):
        self.num = num

    def get_pokes(self):
        result = [0] * self.num
        loc = 0
        for p in range(1, self.num):
            loc = self.insert(p, result, loc)
        result[loc] = self.num
        return result

    @staticmethod
    def insert(p, result, loc):
        result[loc] = p
        num = len(result)
        for _ in range(p + 1):
            while True:
                loc = (loc + 1) % num
                if result[loc] == 0:
                    break
        return loc


if __name__ == "__main__":
    print(CalculatePoke(20).get_pokes())
