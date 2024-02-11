def binary_search(arr, x):
    l, r = 0, len(arr) - 1

    while l <= r:
        pivot = (l + r) // 2
        print(pivot)
        if arr[pivot] == x:
            return pivot
        elif arr[pivot] > x:
            r = pivot - 1
        else:
            l = pivot + 1
    return -1


# https://leetcode.com/problems/binary-search/submissions/1172270350