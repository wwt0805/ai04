"""
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/14 12:07 下午
@Site    : 
@File    : p09_string_match.py
@Software: PyCharm
"""


class StringMatch:
    def __init__(self, s, p):
        self.s = s
        self.p = p

    def match(self):
        if len(self.p) == 0:
            return len(self.s) == 0
        ch = self.p[0]
        if ch == "?":
            return len(self.s) > 0 and StringMatch(self.s[1:], self.p[1:]).match()
        elif ch == "*":
            return StringMatch(self.s, self.p[1:]).match() or len(self.s) > 0 and StringMatch(self.s[1:], self.p).match()  # 去掉*
        else:
            return len(self.s) > 0 and self.s[0] == ch and StringMatch(self.s[1:], self.p[1:]).match()


if __name__ == "__main__":
    print(StringMatch("abaab", "a*b").match(), True)
    print(StringMatch("ab", "a*b").match(), True)
    print(StringMatch("abaaba", "a*b").match(), False)
    print(StringMatch("abaab", "a?aab").match(), True)
    print(StringMatch("abaab", "a?ab").match(), False)
    print(StringMatch("abaaabba", "a?a*bb*").match(), True)
