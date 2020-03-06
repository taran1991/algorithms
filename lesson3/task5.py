
import random

#create matrix
SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

max_negative_elem = None
max_negative_ind = None

for ind, elem in enumerate(arr):
    if elem < 0:
        if max_negative_elem is None or elem > max_negative_elem:
            max_negative_elem = elem
            max_negative_ind = ind

if max_negative_ind is None:
    print('В массиве нет отрицательных элементов')
else:
    print(f'максимальный отрицательный элемент {max_negative_elem}, на позиции {max_negative_ind}')