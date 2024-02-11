def divide(n, m):
    rest = 0
    end = str()

    for d in str(n):
        d = int(d)
        d += rest * 10
        whole = d // m

        if whole:
            rest = d % m
        else:
            rest = d

        end += str(whole)

    end = int(end)
    return end, n % end
