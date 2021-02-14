"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 3:22 下午
@Site    :
@File    : p04_fac.py
@Software: PyCharm
"""


class Factorial:
    def __init__(self, k):
        self.n = k

    def fac(self):
        result = [1]
        while self.n > 1:
            self.mul(result, self.n)
            self.n -= 1
        return self.to_str(result)

    @staticmethod
    def to_str(result):
        s = ""
        for e in result:
            s = str(e) + s
            return s

    @staticmethod
    def mul(result, k):
        add = 0
        for i in range(len(result)):
            r = k * result[i] + add
            result[i] = r % 10
            add = r // 10
        while add > 0:
            result.append(add % 10)
            add //= 10


if __name__ == "__main__":
    for n in range(1, 100 + 1):
        print('%d! = %s' % (n, Factorial(n).fac()))
