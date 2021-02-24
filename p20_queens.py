"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/18 10:08 上午
@Site    : 
@File    : p20_queens.py
@Software: PyCharm
"""


class EightQueens:
    def queens(self, num: int, idx: int = 0, dist: list = None) -> bool:
        """
        （八)皇后问题。由于idx递归调用发生改变，所以采用无参构造。
        :param num:   皇后的个数
        :param idx:   当前皇后的次序
        :param dist:  用于存储递归变量
        :return:      是否有解
        """
        if idx == num:
            return True
        if dist is None:
            dist = []
        for col in range(num):
            if self.available(idx, col, dist):
                dist.append(col)
                if self.queens(num, idx + 1, dist):
                    return True
                del dist[-1]
        return False

    @staticmethod
    def available(row, col, dist):
        for i_row, i_col in enumerate(dist):
            if col == i_col or i_row == col - i_col or row - i_row == i_col - col:
                return False
        return True


num = 8
dist = []
if EightQueens().queens(num, dist=dist):
    for col in dist:
        print(" " * col, end="")
        print("★", end="")
        print("☆" * (num - col - 1))
else:
    print("no solution!")

print(EightQueens.__doc__)




'''
def queens(num: int, idx: int = 0, dist: list = None):
    """

    :param num:
    :param idx:
    :param dist:
    :return:
    """
    if idx == num:
        return True
    if dist is None:
        dist = []
    for col in range(num):
        if available(idx, col, dist):
            dist.append(col)
            if queens(num, idx + 1, dist):
                return True
            del dist[-1]
    return False


def available(row, col, dist):
    for i_row, i_col in enumerate(dist):
        if col == i_col or i_row == col - i_col or row - i_row == i_col - col:
            return False
    return True


dist = []
num = 8
if queens(num, dist=dist):
    for col in dist:
        print(" " * col, end="")
        print("Q", end="")
        print("-" * (num - col - 1))
else:
    print("no solution!")
'''