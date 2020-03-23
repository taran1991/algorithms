
"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""


import random


def test_func(func):
    for _ in range(100):
        m = random.randint(1, 100)
        arr = [random.randint(0, 10) for _ in range(2 * m + 1)]
        median = find_median(arr)
        true_median = sorted(arr)[m]
        assert median == true_median, f'Алгоритм не верен {median} != {true_median}, {arr}'
    print('Функция работает')

def find_median(arr):
    for el1 in arr:
        gr = 0
        less = 0
        eq = -1
        for el2 in arr:
            if el1 > el2:
                gr += 1
            elif el1 < el2:
                less += 1
            else:
                eq += 1
        if min(gr, less) + eq >= max(gr, less):
            return el1


# test_func(find_median)
m = int(input('Введите натуральное число '))
arr = [random.randint(0, 10) for _ in range(2 * m + 1)]
print(arr)
# print(sorted(arr))
median = find_median(arr)
print(median)