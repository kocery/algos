from random import randint


def q_sort(nums, split):
    if len(nums) > 1:
        j = len(nums) - 1
        ind = randint(0, j)
        pivot = nums[ind]
        array[ind], array[j] = array[j], array[ind]
        i = 1

        while i <= j:
            if nums[i] < pivot:
                if nums[j] < pivot:
                    i += 1
                else:
                    i += 1
                    j -= 1
            else:
                if nums[j] > pivot:
                    j -= 1
                else:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j -= 1

        array[j], array[0] = array[0], array[j]

        if j > split:
            q_sort(nums[:j], split)
        elif j < split:
            q_sort(nums[j:], split - j)

    return nums


def sol(arr):
    split = len(arr) // 2
    arr = q_sort(arr, split)
    return arr[split]


array = [1, 14, 13, 11, 15, 1, 4, 2, 7, 11, 10, 14, 9, 10, 12]
print(sol(array))
