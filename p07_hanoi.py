"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/14 11:10 上午
@Site    : 
@File    : p07_hanoi.py
@Software: PyCharm
"""


class Hanoi:
    def __init__(self, src, mid, dst, num):
        """

        :param src: 来源点
        :param mid: 中转点
        :param dst: 目标点
        :param num: 一共有多少盘
        """
        self.src = src
        self.mid = mid
        self.dst = dst
        self.num = num

    def hanuo(self):
        if self.num == 1:
            print("{},{} ==> {}".format(self.src, 1, self.dst))
        else:
            Hanoi(self.src, self.dst, self.mid, self.num - 1).hanuo()
            print("{},{} ==> {}".format(self.src, self.num, self.dst))
            Hanoi(self.mid, self.src, self.dst, self.num - 1).hanuo()


def hanuo(src, mid, dst, num):
    if self.num == 1:
        print("{},{} ==> {}".format(self.src, 1, self.dst))
    else:
        Hanoi(self.src, self.dst, self.mid, self.num - 1).hanuo()
        print("{},{} ==> {}".format(self.src, self.num, self.dst))
        Hanoi(self.mid, self.src, self.dst, self.num - 1).hanuo()



if __name__ == "__main__":
    Hanoi("A", "B", "C", 4).hanuo()
