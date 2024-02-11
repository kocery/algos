from random import randint


def karat(x, y):
    if len(str(x)) < 3 or len(str(y)) < 3:
        return x * y

    n = max(len(str(x)), len(str(y))) // 2

    a, b = x // 10 ** n, x % 10 ** n
    c, d = y // 10 ** n, y % 10 ** n

    s0 = karat(b, d)
    s1 = karat((a + b), (c + d))
    s2 = karat(a, c)

    return ((10 ** (n * 2)) * s2) + ((10 ** n) * (s1 - s2 - s0)) + s0


test = [(randint(2**50, 2**100), randint(2**50, 2**100)) for _ in range(50)]

for a, b in test:
    kar = karat(a, b)
    print(a, b, a * b == kar)
