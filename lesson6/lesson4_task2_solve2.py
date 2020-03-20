import math

# num = 100
# num = 200
# num = 400
num = 800
# num = 10000

MULTIPLIER = 1.3
size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30

prime_num = 0
for n in range(2, size):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        prime_num += 1
        if prime_num == num:
            # print(n)
            break