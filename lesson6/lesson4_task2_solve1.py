import math

# num = 100
# num = 200
# num = 400
num = 800
# num = 10000

MULTIPLIER = 1.3
size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30
prime_num = 0
sieve = [i for i in range(size)]
sieve[1] = 0
for i in range(2, size):
    if sieve[i] != 0:
        prime_num += 1
        if prime_num == num:
            break
            # print(i)
        j = i + i
        while j < size:
            sieve[j] = 0
            j += i