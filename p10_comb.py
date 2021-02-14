"""
C(5, 2) = 10
C(6, 3) = 20
C(4, 2) = 6

C(n, m) = ? 0 <= m <= n
"""


def comb(n, m):
    if m == 0 or m == n:
        return 1
    if m == 1:
        return n
    return comb(n - 1, m - 1) + comb(n - 1, m)


for n in range(1, 10 + 1):
    for m in range(n + 1):
        print("C({}, {}) = {}".format(n, m, comb(n, m)))

