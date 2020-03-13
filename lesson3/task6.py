
import random

#create matrix
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
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

if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

elem_sum = 0
if max_ind - min_ind > 1:
    for ind in range(min_ind + 1, max_ind):
        elem_sum += arr[ind]

print(elem_sum)