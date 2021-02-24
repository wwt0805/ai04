"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/17 8:58 下午
@Site    : 
@File    : p12_train.py
@Software: PyCharm
"""


def get_train(n):
    if n <= 1:
        return 1
    result = 0
    for i in range(n):
        result += get_train(i) * get_train(n - 1 - i)
    return result


def get_train2(n, store=None):
    if store is None:
        store = {}
    if n <= 1:
        return 1
    if n in store:
        return store[n]
    result = 0
    for i in range(n):
        result += get_train2(i) * get_train2(n - 1 - i)
    store[n] = result
    return result


if __name__ == "__main__":
    for n in range(10 + 1):
        print('get_train(%d) = %d' % (n, get_train(n)))
        print('get_train(%d) = %d' % (n, get_train2(n)))

