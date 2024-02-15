from random import randint


def divide(a, b):
    if b == 0:
        raise ValueError("Делитель не может быть равен нулю")

    q, r = 0, 0

    for digit in str(a):
        cur = int(digit) + r * 10

        q_digit = 0
        while cur >= b:
            cur -= b
            q_digit += 1

        q = q * 10 + q_digit
        r = cur

    return q


test = [(randint(2 ** 50, 2 ** 100), randint(2 ** 50, 2 ** 100)) for _ in range(50)]

for a, b in test:
    div = divide(a, b)
    print(a, b, a // b == div)
