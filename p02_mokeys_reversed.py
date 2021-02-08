'''
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 11:08 上午
@Site    : 
@File    : p02_mokeys_reversed.py
@Software: PyCharm
'''
def get_peaches(monkeys):
    unit = 1
    while True:
        ok, peach = divide((monkeys-1) * unit, monkeys)
        if ok:
            return peach
        unit += 1

def divide(peaches, monkeys):
    for _ in range(monkeys):
        if peaches % (monkeys - 1) == 0:
            peaches = peaches // (monkeys - 1) * monkeys + 1
        else:
            return False, 0
    return True, peaches

print(get_peaches(5))