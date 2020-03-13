
import random

#create matrix
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 4
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

nums_quantity = {}

for elem in arr:
    nums_quantity[elem] = nums_quantity.setdefault(elem, 0) + 1

most_common_num = 0
freq = 0

for key, val in nums_quantity.items():
    if val > freq:
        most_common_num = key
        freq = val

print(most_common_num)
