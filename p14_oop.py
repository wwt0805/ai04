"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/23 8:19 下午
@Site    :
@File    : p14_oop.py
@Software: PyCharm
"""


class A:
    def __add__(self, other):
        print("in __add__")
        print(other)

    def __radd__(self, other):  # 右加，对象在右边，比如 3 + a，只有算术运算有
        pass

    def __sub__(self, other):
        pass

    def __str__(self):
        print("in __str__()")

    def __repr__(self):   ### repr和str都能打印出字符串结果，但是如果都定义了str优先级高于repr
        print()
        return "ddd"

    def __reversed__(self):
        print("in __reversed__()")

    def __mul__(self, other):
        pass

    def __truediv__(self, other):  # 除法
        pass

    def __divmod__(self, other):  # 整除求余
        pass

    def __idiv__(self, other):  # 存疑
        pass

    def __pow__(self, power, modulo=None):  # **
        pass

    def __neg__(self):   # 取反-
        pass

    def __xor__(self, other):  # ^
        pass

    def __or__(self, other):  # |
        pass

    def __and__(self, other):  # &
        pass

    def __invert__(self):  # ~
        print("invert")

    def __mod__(self, other):  # %
        print("in mod")

    def __lshift__(self, other):  # << 左移
        pass

    def __rshift__(self, other):  # >> 右移
        pass


if __name__ == "__main__":
    a = A()
    b = a + 3  # a.__add__(3)
    print(b)   # None

    b = a - 3   # a.__sub__(3)
    b = a * 3   # a.__mul__(3)
    b = a / 3   # a.__truediv__(3)
    # b = a // 3  # a.__idiv__(3)
    b = a ** 3  # a.__pow__(3)
    b = -a      # a.__neg__(3)
    b = ~a      # a.__invert__(3)
    b = a % 3   # a.__mod__(3)

