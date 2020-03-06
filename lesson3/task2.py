
import random

#create matrix
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

ind_arr = [ind for ind, elem in enumerate(arr) if elem % 2 == 0]

print(arr)
print(ind_arr)