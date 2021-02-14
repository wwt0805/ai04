"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 11:08 上午
@Site    :
@File    : p02_mokeys_reversed.py
@Software: PyCharm
"""



class SplitPeaches:
    def __init__(self, monkeys):
        """
        :param monkeys: 猴子的数目
        """
        self.monkeys = monkeys

    def get_peaches(self):
        unit = 1
        while True:
            ok, peach = self.divide((self.monkeys - 1) * unit, self.monkeys)
            if ok:
                return peach
            unit += 1

    @staticmethod
    def divide(peaches, monkeys):
        for _ in range(monkeys):
            if peaches % (monkeys - 1) == 0:
                peaches = peaches // (monkeys - 1) * monkeys + 1
            else:
                return False, 0
        return True, peaches


if __name__ == "__main__":
    print(SplitPeaches(5).get_peaches())
