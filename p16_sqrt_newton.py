"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/24 9:24 下午
@Site    :
@File    : p16_sqrt_newton.py
@Software: PyCharm
"""


def sqrt(a, n=2):                   # 牛顿法求平方根函数
    x = 1                           # 赋初值，如果初值为正则求得正平方根，否则为负平方根
    y = lambda x: x ** n            # lambda函数定义所求函数式   注意lambda表达式必须有返回值(y)!!!
    dy_dx = lambda x: 2 * x         # lambada函数定义导函数式
    delta_y = lambda x: a - y(x)
    delta_x = lambda x: delta_y(x) / dy_dx(x)  # 牛顿法定义

    # dx = dy / y' = (a - x ** 2) / 2x
    # x' = x + dx = (a + x ** 2) / 2x

    for _ in range(10):
        x += delta_x(x)
    return x


if __name__ == "__main__":
    for x in range(1, 10 + 1):
        print("sqrt({}) = {}".format(x, sqrt(x)))
