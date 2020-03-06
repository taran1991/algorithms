
import random

#create matrix
SIZE = 7
MIN_ITEM = 0
MAX_ITEM = 10
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if len(arr) < 2:
    print('Введите массив состоящий как минимум из дух элементов')
    exit()

if arr[0] < arr[1]:
    min_elem1 = arr[0]
    min_elem2 = arr[1]
else:
    min_elem1 = arr[1]
    min_elem2 = arr[0]

for i in range(2, SIZE):
    if arr[i] < min_elem1:
        min_elem1, min_elem2 = arr[i], min_elem1
    elif arr[i] < min_elem2:
        min_elem2 = arr[i]

print(min_elem1, min_elem2)
