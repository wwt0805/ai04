"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/24 10:49 下午
@Site    :
@File    : p19_two_x.py
@Software: PyCharm
"""


def solve():
    y = lambda x1, x2: (x1 - 3) ** 2 + (x2 + 2) ** 2
    dy_dx1 = lambda x1, x2: 2 * (x1 - 3)
    dy_dx2 = lambda x1, x2: 2 * (x2 + 2)
    dx1 = lambda lr, x1, x2: - lr * dy_dx1(x1, x2)
    dx2 = lambda lr, x1, x2: - lr * dy_dx2(x1, x2)
    # 或将上式写为 dx = lambda x1, x2, lr:( -lr * dy_dx1(x1, x2), -lr * dy_dx2(x1, x2))

    x1, x2 = 1, 1
    lr = 0.01
    for _ in range(1000):
        x1 += dx1(lr, x1, x2)
        x2 += dx2(lr, x1, x2)
    return x1, x2


def practise():
    """
    求解 y = -3 * x ** 4 + 20 * x ** 2 + 10 * x + 9的最大值
    :return:
    """
    y = lambda x: 3 * x ** 4 - 20 * x ** 2 - 10 * x - 9  # 求原式最大等价于求该式最小
    dy_dx = lambda x: 12 * x ** 3 - 40 * x - 10          # y的导函数
    dx = lambda x, lr: -lr * dy_dx(x)

    x = 1
    lr = 0.01
    for _ in range(1000):
        x += dx(x, lr)
    return x


if __name__ == "__main__":
    print(solve())
    print(practise())

