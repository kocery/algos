def lsd_radix_sort(arr):
    for i in range(len(arr[0]) - 1, -1, -1):
        counting_sort(arr, i)

    return arr


def counting_sort(arr, index):
    count = [0] * 1114112  # full unicode range
    output = [0] * len(arr)

    for s in arr:
        count[ord(s[index])] += 1

    for i in range(1, 1114112):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        index_s = ord(arr[i][index])
        output[count[index_s] - 1] = arr[i]
        count[index_s] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


arr = ["🤓👣🤓", "🤖😳👅", "👻😈👀", "🤬🤙👸", "🤫🤫🤬", "👉👈😔", "🤠🤜🤡"]  # cursed
lsd_radix_sort(arr)
print(arr)
