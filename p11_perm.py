def perm(n: int, m: int):
    if m == 0:
        return 1
    if m == 1:
        return n
    # include the first ball
    result = m * perm(n - 1, m - 1)
    # m = 3,   ^3^12^
    if n > m:
        result += perm(n - 1, m - 1)   # Not include first ball
    return result


for n in range(1, 10 + 1):
    for m in range(n + 1):
        print("P({}, {}) = {}".format(n, m, perm(n, m)))
