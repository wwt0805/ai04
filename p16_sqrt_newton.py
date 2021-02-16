def sqrt(a, n=3):
    # return: a ** (1/n)
    x = 1
    y = lambda x: x ** n
    dy_dx = lambda x: n * x ** (n - 1)
    delta_y = lambda x: a - y(x)
    delta_x = lambda x: delta_y(x) / dy_dx(x)

    for _ in range(10):
        x += delta_x(x)
    return x


for x in range(1, 10 + 1):
    print("sqrt({}) = {}".format(x, sqrt(x)))
