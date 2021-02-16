class Frac:
    def __init__(self, a, b):
        m = gcd(a, b)
        self.a = a // m
        self.b = b // m

    def __repr__(self):
        return "{}/{}".format(self.a, self.b)

    def __add__(self, other):
        other = to_frac(other)
        return Frac(self.a * other.b + self.b * other.a, self.b * other.b)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Frac(self.a * other.b - self.b * other.a, self.b * other.b)

    def __rsub__(self, other):
        other = to_frac(other)
        return Frac(other.a * self.b - other.b * self.a, self.b * other.b)

    def __neg__(self):
        return Frac(- self.a, self.b)

    def __mul__(self, other):
        other = to_frac(other)
        return Frac(other.a * self.a, other.b * self.b)

    def __truediv__(self, other):
        other = to_frac(other)
        return Frac(other.a * self.b, other.b * self.a)


def to_frac(value):
    if isinstance(value, Frac):
        return value
    if type(value) == int:
        return Frac(value, 1)
    raise Exception('expect an integer, but found {}'.format(value))


def gcd(a, b):  # 辗转相除法
    if a > b:
        t = a
        a = b
        b = t
    while a != 0:
        t = b % a
        b = a
        a = t
    return b


f1 = Frac(-3, 4)
f2 = Frac(2, 3)
# print(f1, "+", f2, "=", f1 + f2)

# print('-', f1, "=", -f1)
# print(f1, "+", 3, f1 + 3)
# print('-', f1, "=", -f1)
print(f1, "*", f2, "=", f1 * f2)
print(f1, "/", f2, "=", f1 / f2)
