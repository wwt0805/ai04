"""
# -*- coding: utf-8 -*-
Author Wu Wentong
@Time    : 2021/2/6 10:45 上午
@Site    :
@File    : p01_monkeys.py
@Software: PyCharm
"""
'''
    五猴分桃问题
        有五个猴子上山采桃，约定第二天来分桃。第二天早上来了一只猴子，他先把桃子分成了
    五份，然后发现多了一个，就自己吃了，并且带走了自己的那份。过了一会又来了一只猴子，它
    做了同样的动作，也吃了多出的一个桃子，带走了自己那份。后来的第二第四第五只猴子都是这
    样做的，请问最初有多少个桃子。
    
    思路：
    1. 桃子数p=1
    2. 如果p能被5个猴子分掉（函数），p就是桃子数目，程序结束
    3. 否则p=p+1
    4. 转2
    
    p能否被5个猴子分掉函数
    1. 猴子数m=1
    2. 如果m<5, 则
        a. 否则p=p-1
        b. 如果p能被5整除，则：
            p = p / 5 * 4
            m = m + 1
            转2
        c. 否则（p不能被5整除），程序结束，返回"False"
    3. 表示5个猴子都分完了，程序成功，返回"True"
'''


class SplitPeaches:
    def __init__(self, monkeys):
        """
        :param monkeys: 猴子的数目
        """
        self.monkeys = monkeys

    def dividable(self, p):
        for _ in range(self.monkeys):
            p -= 1
            if p % self.monkeys == 0:
                p = p // self.monkeys * (self.monkeys - 1)
            else:
                return False
        return True

    def get_peaches(self):
        p = 1
        while not self.dividable(p):
            p += 1
        return p


print(SplitPeaches(5).get_peaches())  # 返回5个猴子拿走的数目
