def rec_minus(n, m):
    len_n, len_m = len(str(n)), len(str(m))
    k = len_n - len_m - 1 if len_n != len_m else 0
    c = 0

    while n >= m:
        n -= m * 10 ** k
        c += 1

    return c


def divide(n, m):
    end = '0'

    while n >= m:
        len_n, len_m = len(str(n)), len(str(m))
        k = len_n - len_m - 1 if len_n != len_m else 0

        if n - m * 10 ** k > 0:
            c = rec_minus(n, m * 10 ** k)
            n -= m * 10 ** k * c
            end += str(c)
            if n < m * 10 ** (k - 1) and k != 0:
                end += '0'

    return int(end)
