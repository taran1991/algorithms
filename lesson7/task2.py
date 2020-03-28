
"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


SIZE = 10


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[0: middle])
        right = merge_sort(arr[middle:])
        i, j = 0, 0
        for ind in range(len(arr)):
            if i == len(left):
                arr[ind:] = right[j:]
                break
            elif j == len(right):
                arr[ind:] = left[i:]
                break
            if left[i] <= right[j]:
                arr[ind] = left[i]
                i += 1
            else:
                arr[ind] = right[j]
                j += 1
    return arr


arr = [random.uniform(0, 50) for _ in range(SIZE)]
print(arr)
print('*' * 50)
merge_sort(arr)
print(arr)

