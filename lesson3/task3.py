
import random

#create matrix
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if not arr:
    print('Введен пустой список')
    exit()

max_num = arr[0]
min_num = arr[0]
max_ind = 0
min_ind = 0

for ind, elem in enumerate(arr):
    if elem > max_num:
        max_num = elem
        max_ind = ind
    if elem < min_num:
        min_num = elem
        min_ind = ind

arr[min_ind] = max_num
arr[max_ind] = min_num
print(arr)