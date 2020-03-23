import math

# num = 100
# num = 200
# num = 400
num = 800
# num = 10000

MULTIPLIER = 1.3
size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30

array = [True for _ in range(size)]
array[:2] = [False, False]
count = 0

for i in range(2, size):
    if array[i]:
        count += 1
        if count == num:
            # print(i)
            break
        for j in range(i ** 2, size, i):
            array[j] = False