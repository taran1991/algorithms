
# -*- coding: utf-8 -*-


"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена». Второй — без использования «Решета Эратосфена».
"""


import timeit
import cProfile


def test_func(func):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for ind, elem in enumerate(primes, start=1):
        assert func(ind) == elem
    print('Тест пройден')


#Решени1, с «Решето Эратосфена»
def find_prime_sieve(num, n=10):
    if num == 0:
        raise ValueError('num не может быть 0')
    prime_num = 0
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            prime_num += 1
            if prime_num == num:
                return i
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    return find_prime_sieve(num, n=n * 10)

test_func(find_prime_sieve) # функция работает корректно

print(timeit.timeit('find_prime_sieve(10)', globals=globals(), number=10000)) # 0.23207452099995862
print(timeit.timeit('find_prime_sieve(20)', globals=globals(), number=10000)) # 0.26666180799998074
print(timeit.timeit('find_prime_sieve(30)', globals=globals(), number=10000)) # 2.851207670000008
print(timeit.timeit('find_prime_sieve(40)', globals=globals(), number=10000)) # 2.9201756229999773
print(timeit.timeit('find_prime_sieve(50)', globals=globals(), number=10000)) # 3.043090473999996
print(timeit.timeit('find_prime_sieve(100)', globals=globals(), number=10000)) # 3.706014433000064
print(timeit.timeit('find_prime_sieve(1000)', globals=globals(), number=10000)) # 45.22330281699999

cProfile.run('find_prime_sieve(10)') # 2/1    0.000    0.000    0.000    0.000 task2.py:22(find_prime_sieve)
cProfile.run('find_prime_sieve(20)') # 2/1    0.000    0.000    0.000    0.000 task2.py:22(find_prime_sieve)
cProfile.run('find_prime_sieve(30)') # 3/1    0.000    0.000    0.000    0.000 task2.py:22(find_prime_sieve)
cProfile.run('find_prime_sieve(40)') # 3/1    0.000    0.000    0.000    0.000 task2.py:22(find_prime_sieve)
cProfile.run('find_prime_sieve(50)') # 3/1    0.000    0.000    0.000    0.000 task2.py:22(find_prime_sieve)
cProfile.run('find_prime_sieve(100)') # 3/1    0.000    0.000    0.000    0.000 task2.py:22(find_prime_sieve)
cProfile.run('find_prime_sieve(1000)') # 4/1    0.004    0.001    0.004    0.004 task2.py:22(find_prime_sieve)

#Решени1, без «Решето Эратосфена»
def find_prime(num, start=2, end=10, prime_num=0):
    if num == 0:
        raise ValueError('num не может быть 0')
    for n in range(start, end):
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            prime_num += 1
            if prime_num == num:
                return n
    return find_prime(num, start=end, end=end*10, prime_num=prime_num)

test_func(find_prime) # функция работает корректно

print(timeit.timeit('find_prime(10)', globals=globals(), number=10000)) # 0.14626312000018515
print(timeit.timeit('find_prime(20)', globals=globals(), number=10000)) # 0.5540236940000796
print(timeit.timeit('find_prime(30)', globals=globals(), number=10000)) # 1.3123084630001358
print(timeit.timeit('find_prime(40)', globals=globals(), number=10000)) # 2.5121495459998187
print(timeit.timeit('find_prime(50)', globals=globals(), number=10000)) # 4.745956364999984
print(timeit.timeit('find_prime(100)', globals=globals(), number=10000)) # 21.43437609900002
print(timeit.timeit('find_prime(200)', globals=globals(), number=10000)) # 110.40081433499995

""" 
print(timeit.timeit('find_prime(1000)', globals=globals(), number=10000))
# не стал проверять, потому что похоже на квадратичную зависимость, пришлось бы ждать окло 25 мин
 """

cProfile.run('find_prime(10)') # 2/1    0.000    0.000    0.000    0.000 task2.py:57(find_prime)
cProfile.run('find_prime(20)') # 2/1    0.000    0.000    0.000    0.000 task2.py:57(find_prime)
cProfile.run('find_prime(30)') # 3/1    0.000    0.000    0.000    0.000 task2.py:57(find_prime)
cProfile.run('find_prime(40)') # 3/1    0.000    0.000    0.000    0.000 task2.py:57(find_prime)
cProfile.run('find_prime(50)') # 3/1    0.001    0.000    0.001    0.001 task2.py:57(find_prime)
cProfile.run('find_prime(100)') # 3/1    0.002    0.001    0.002    0.002 task2.py:57(find_prime)
cProfile.run('find_prime(1000)') # 4/1    0.408    0.102    0.408    0.408 task2.py:57(find_prime)

"""
Вывод:
Хотя вариант с «Решето Эратосфена» на малых данных берет больше времени, данный метод возрастает гороздо медленнее,
чем второй вариант. Мне кажется что во втором варианте квадратичная асимптотика(хотя я не уверен из-за последней точки)
O(N^2), а в первом, наверное, логорифмическая O(n*log(n)).
"""