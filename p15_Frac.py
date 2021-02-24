"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/23 8:19 下午
@Site    :
@File    : p15_Frac.py
@Software: PyCharm
"""


class Frac:
    def __init__(self, a, b):
        """

        :param a:  a表示分子
        :param b:  b表示分母
        """
        m = gcd(a, b)    # gcd最大公约数函数
        self.a = a // m
        self.b = b // m

    def __repr__(self):  # 定义打印函数，若打印都需要重定义__repr__
        return "{}/{}".format(self.a, self.b)

    def __add__(self, other):
        other = to_frac(other)  # 将非分数转化为分数
        return Frac(self.a * other.b + self.b * other.a, self.b * other.b)

    def __radd__(self, other):
        return self.__add__(other)  # 右边相加和左边相加结果一致，所以直接调用__add__即可

    def __sub__(self, other):
        return Frac(self.a * other.b - self.b * other.a, self.b * other.b)

    def __rsub__(self, other):
        other = to_frac(other)
        return Frac(other.a * self.b - other.b * self.a, self.b * other.b)

    def __neg__(self):
        return Frac(- self.a, self.b)

    def __mul__(self, other):
        other = to_frac(other)
        return Frac(other.a * self.a, other.b * self.b)

    def __truediv__(self, other):
        other = to_frac(other)
        return Frac(other.a * self.b, other.b * self.a)


def to_frac(value):
    if isinstance(value, Frac):  # 如果本身就是Frac分数就返回本身
        return value
    if type(value) == int:       # 如果它本身是整数，返回分子为对应整数，分母为1即可
        return Frac(value, 1)
    raise Exception('expect an integer, but found {}'.format(value))


def gcd(a, b):  # 辗转相除法找最大公约数
    if a > b:
        t = a
        a = b
        b = t  # t -> a, a-> b, b ->t, 这样就是b > a
    while a != 0:
        t = b % a
        b = a
        a = t
    return b


if __name__ == "__main__":
    f1 = Frac(-3, 4)
    f2 = Frac(2, 3)
    print(f1, "+", f2, "=", f1 + f2)
    print(f1, "-", f2, "=", f1 - f2)
    print("-", f1, "=", -f1)
    print(f1, "+", 3, f1 + 3)
    print(3, "+", f1, "=", 3 + f1)
    print(f1, "*", f2, "=", f1 * f2)
    print(f1, "/", f2, "=", f1 / f2)
