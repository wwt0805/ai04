"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/24 10:30 下午
@Site    :
@File    : p18_sqrt_GD2.py
@Software: PyCharm
"""


def sqrt(a, n=2):
    """

    :param a: 底数
    :param n: 次方数，默认为2
    :return:  返回底数的次方根
    """
    y = lambda x: (x ** n - a) ** 2
    dy_dx = lambda x: 2 * (x ** n - a) * n * x ** (n - 1)
    dx = lambda x, lr: - lr * dy_dx(x)

    lr = 0.01
    x = 1.0
    for _ in range(1000):
        x += dx(x, lr)
    return x


if __name__ == "__main__":
    for x in range(1, 11):
        print("sqrt({}) = {}".format(x, sqrt(x)))