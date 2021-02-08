'''
coding=utf-8
Author Wu Wentong
@Time    : 2021/2/6 12:23 下午
@Site    : 
@File    : p03_pokes_seq.py
@Software: PyCharm
'''
def  get_pokes(num):
    result = [0] * num
    loc = [e for e in range(num)]
    for p in range(1, num):
        move(p, result, loc)
    result[loc[0]] = num
    return result

def move(p, result, loc):
        first = loc[0]
        del loc[0]
        result[first] = p
        for _ in range(p):
            first = loc[0]
            del loc[0]
            loc.append(first)
    # result[loc[0]] = num

print(get_pokes(20))