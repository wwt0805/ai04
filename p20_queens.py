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
        :param num:   皇后的数量
        :param idx:   表示当前处理的是第几个皇后
        :param dist:  之前皇后的分布
        :return:      返回bool值表示当前个数皇后是否有解
        """
        if idx == num:  # 表示当前已处理完
            return True
        if dist is None:
            dist = []
        for col in range(num):
            if self.available(idx, col, dist):       # 判断把当前idx序号的皇后放在第col列且前面有dist的皇后，是否可行
                dist.append(col)                     # 若当前idx的皇后可行，则添加至分布列表dist中
                if self.queens(num, idx + 1, dist):  # 继续验证下一个（idx+1）次序的皇后是否可行
                    return True                      # 若以上条件都满足return True
                del dist[-1]                         # 若idx+1皇后不满足，则说明dist中存储的最后一个皇后位置不合适，需要删除重新验证
        return False                                 # 若col和idx+1验证都不满足则返回False，说明当前个数的皇后无解。

    @staticmethod
    def available(row, col, dist):
        for i_row, i_col in enumerate(dist):        # 获取dist中存储皇后的位置，接下来需要验证与当前皇后是否有互斥关系
            # 互斥条件：1. dist中的皇后和当前皇后在同一列；2.两者在斜线上（用绝对值即可表示所有情况）
            if col == i_col or abs(row - i_row) == abs(i_col - col):
                return False
        return True


if __name__ == "__main__":
    for num in range(1, 9):
        dist = []
        print("n = {}".format(num))
        if EightQueens().queens(num, dist=dist):
            for col in dist:
                print(" " * col, end="")
                print("★", end="")
                print("☆" * (num - col - 1))
            print("=" * 10)
        else:
            print("no solution!")
            print("=" * 10)


