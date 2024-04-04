from random import randint


def q_sort(nums, split, left=None, right=None):
    left = left if left else 0
    right = right if right else len(nums)

    if right <= left + 1:
        return nums[left]

    i, j = left, right - 1

    pivot = nums[randint(left, right - 1)]
    while True:
        while i <= j and nums[i] < pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1

    if (i == split and nums[i] == pivot) or (j == split and nums[j] == pivot):
        return pivot
    if i > split:
        return q_sort(nums, split, left, i)

    return q_sort(nums, split, j + 1, right)


def sol(arr):
    split = len(arr) // 2
    return q_sort(arr, split)


array = [1, 14, 13, 11, 15, 1, 4, 2, 7, 11, 10, 14, 9, 10, 12]
print(sol(array))
