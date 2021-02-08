'''
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 11:49 上午
@Site    : 
@File    : p03_pokes.py
@Software: PyCharm
'''
def get_pokes(num):
    result = [num]
    p = num - 1
    while p > 0:
        insert(p, result)
        p -= 1
    return result

def insert(p, result):
    for _ in range(p):
        last = result[-1]
        del result[-1]
        result.insert(0, last)
    result.insert(0, p)

print(get_pokes(20))