
import random

#create matrix
ROW_SIZE = 7
COLUMN_SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ROW_SIZE)] for _ in range(COLUMN_SIZE)]
print(matrix)

arr_of_mins = []

for i in range(COLUMN_SIZE):
    arr_of_mins.append(matrix[i][0])
    for elem in matrix[i]:
        if elem < arr_of_mins[i]:
            arr_of_mins[i] = elem
print(arr_of_mins)

max_elem = arr_of_mins[0]
for elem in arr_of_mins:
    if elem > max_elem:
        max_elem = elem
print(max_elem)
