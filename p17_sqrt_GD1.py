def sqrt(a, n=2):
    y = lambda x: x ** n
    dy_dx = lambda x: n * x ** (n - 1)
    dy = lambda x: a - y(x)
    dx = lambda x, lr: lr * dy(x) * dy_dx(x)

    lr = 0.001
    x = 1.0
    for _ in range(200):
        x += dx(x, lr)
    return x


for x in range(1, 10 + 1):
    print("sqrt({}) = {}".format(x, sqrt(x)))
