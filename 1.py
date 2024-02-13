from random import randint


def divide(a, b):
    n, m = len(str(a)), len(str(b))
    c = 0

    while a > b:
        for i in range(n - m + 1):
            num = 0
            k = 10 ** (n - m - i)
            while (num + 1) * b < a / k:
                num += 1
            a -= num * b * k
            c += num * k

    return c


test = [(randint(2 ** 50, 2 ** 100), randint(2 ** 50, 2 ** 100)) for _ in range(50)]

for a, b in test:
    div = divide(a, b)
    print(a, b, a // b == div)
