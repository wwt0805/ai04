'''
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 10:45 上午
@Site    : 
@File    : p01_monkeys.py
@Software: PyCharm
'''
def get_peaches(monkeys):            # 定义桃子总数的函数
    p = 1                            # 定义初始的桃子数目
    while not dividable(p, monkeys): # 如果当前桃子数目对于猴子数目不可分
        p += 1                       # 桃子数目+1，继续循环
    return p                         # 若能分返回当前桃子数目

def dividable(p, m):
    for _ in range(m):
        p -= 1
        if p % m == 0:
            p = p // m * (m - 1)
        else:
            return False
    return True

print(get_peaches(5))  # 返回5个猴子拿走的数目
