"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/14 10:34 上午
@Site    :
@File    : p06_guess_name.py
@Software: PyCharm
"""
import math


class ChooseName:
    def __init__(self, names):
        self.names = names

    def guess_name(self):
        lines = self.get_lines(self.names)
        while True:
            answers = []
            for line in lines:
                print(", ".join(line))
                answer = input("Is your name in this paper?(y/n)")
                answer = 1 if answer in ("Y", "y") else 0
                answers.append(answer)
            name = self.get_name(answers, self.names)
            print("Your name is:{}".format(name))
            answer = input("Continue?(y/n)")
            if answer not in ("Y", "y"):
                break

    @staticmethod
    def get_lines(names):
        rows = int(math.log2(len(names))) + 1
        lines = [[] for _ in range(rows)]
        for i, name in enumerate(names):
            id = i + 1
            for j in range(rows):
                if id % 2 == 1:
                    lines[j].append(name)
                id //= 2
        return lines

    @staticmethod
    def get_name(answers, names):
        id = 0
        for digit in reversed(answers):
            id = id * 2 +  digit
        return "不存在的姓" if id == 0 else names[id - 1]


if __name__ == "__main__":
    ChooseName("赵钱孙李周吴郑").guess_name()
