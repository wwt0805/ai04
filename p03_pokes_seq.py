"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 12:23 下午
@Site    :
@File    : p03_pokes_seq.py
@Software: PyCharm
"""


class CalculatePoke:
    def __init__(self, num):
        self.num = num

    def get_pokes(self):
        result = [0] * self.num
        loc = [e for e in range(self.num)]
        for p in range(1, self.num):
            self.move(p, result, loc)
        result[loc[0]] = self.num
        return result

    @staticmethod
    def move(p, result, loc):
        first = loc[0]
        del loc[0]
        result[first] = p
        for _ in range(p):
            first = loc[0]
            del loc[0]
            loc.append(first)


if __name__ == "__main__":
    print(CalculatePoke(20).get_pokes())
