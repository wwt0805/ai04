'''
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 3:22 下午
@Site    : 
@File    : p04_fac.py
@Software: PyCharm
'''

def fac(n):
    result = [1]
    while n > 1:
        mul(result, n)
        n -= 1
    return to_str(result)

def to_str(result):
    s = ""
    for e in result:
        s = str(e) + s
        return s

def mul(result, n):
    add = 0
    for i in range(len(result)):
        r = n * result[i] + add
        result[i] = r % 10
        add = r // 10
    while add > 0:
        result.append(add % 10)
        add //= 10

for n in range(1, 100+1):
    print('%d! = %s' % (n, fac(n)))