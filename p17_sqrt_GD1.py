"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/24 10:02 下午
@Site    : 
@File    : p17_sqrt_GD1.py
@Software: PyCharm
"""


def sqrt(a, n=2):
    """

    :param a: 底数
    :param n: 次方
    :return:  底数对应的次方根
    """
    y = lambda x: x ** n
    dy_dx = lambda x: n * x ** (n - 1)
    dy = lambda x: a - y(x)
    dx = lambda x, lr: lr * dy(x) * dy_dx(x)

    lr = 0.01
    x = 1.0
    for _ in range(1000):
        x += dx(x, lr)
    return x


if __name__ == "__main__":
    for x in range(1, 11):
        print("sqrt({}) = {}".format(x, sqrt(x)))