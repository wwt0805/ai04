"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/16 3:40 下午
@Site    : 
@File    : p17_sqrt_GD.py
@Software: PyCharm
"""


def sqrt(a, n=2):
    """

    :param a:  底数
    :param n:  次方，默认为2
    :return:   返回底数的次方根
    """
    y = lambda x: x ** n
    dy_dx = lambda x: n * x ** (n - 1)
    dy = lambda x: a - y(x)
    dx = lambda x, lr: lr * dy(x) * dy_dx(x)

    lr = 0.001
    x = 1.0
    for _ in range(200):
        x += dx(x, lr)
    return x


for x in range(1, 11):
    print("sqrt({}) = {}".format(x, sqrt(x)))