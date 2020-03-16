
# -*- coding: utf-8 -*-

"""Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Я выбрал 2 задачу из 2-ой практической работы. Не самая интересная, но я решил ее через рекурсию и мне было
интересно сравнить данное решение с другими алгоритмоми.

Задача:
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import timeit
import cProfile

#функция проверки
def test_func(func):
    num = 0
    test_odd = 0
    test_even = 0
    for i in range(1, 10):
        num += i * 10 ** (i - 1)
        if i % 2 == 0:
            test_even += 1
        else:
            test_odd += 1
        odd, even = func(num)
        assert odd == test_odd
        assert even == test_even
        print(f'{num} - число, {even} четных цифр, {odd} нечетных цифр')
    odd, even = func(1000)
    assert odd == 1
    assert even == 3
    print(f'{1000} - число, {even} четных цифр, {odd} нечетных цифр')
    print('Тест пройден')


#Решение 1, рекурсия

def increase_odd_or_even(num, odd, even):
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    return odd, even

def count_odd_even_digits(num, odd=0, even=0):
    if num // 10 == 0:
        return increase_odd_or_even(num, odd, even)
    else:
        digit = num % 10
        num = num // 10
        odd, even =increase_odd_or_even(digit, odd, even)
        return count_odd_even_digits(num, odd, even)

test_func(count_odd_even_digits) # функция работает корректно

print(timeit.timeit('count_odd_even_digits(6 * 10 ** 5)', globals=globals())) # 3.2623128589984844
print(timeit.timeit('count_odd_even_digits(6 * 10 ** 10)', globals=globals())) # 6.206482053996297
print(timeit.timeit('count_odd_even_digits(6 * 10 ** 15)', globals=globals())) # 9.595676280994667
print(timeit.timeit('count_odd_even_digits(6 * 10 ** 20)', globals=globals())) # 14.571754146003514
print(timeit.timeit('count_odd_even_digits(6 * 10 ** 40)', globals=globals())) # 29.172894343995722
print(timeit.timeit('count_odd_even_digits(6 * 10 ** 80)', globals=globals())) # 61.26052269000502

cProfile.run('count_odd_even_digits(6 * 10 ** 5)') # 6/1    0.000    0.000    0.000    0.000 task1.py:52(count_odd_even_digits)
cProfile.run('count_odd_even_digits(6 * 10 ** 10)') # 11/1    0.000    0.000    0.000    0.000 task1.py:52(count_odd_even_digits)
cProfile.run('count_odd_even_digits(6 * 10 ** 15)') # 16/1    0.000    0.000    0.000    0.000 task1.py:52(count_odd_even_digits)
cProfile.run('count_odd_even_digits(6 * 10 ** 20)') # 21/1    0.000    0.000    0.000    0.000 task1.py:52(count_odd_even_digits)
cProfile.run('count_odd_even_digits(6 * 10 ** 40)') # 41/1    0.000    0.000    0.000    0.000 task1.py:52(count_odd_even_digits)
cProfile.run('count_odd_even_digits(6 * 10 ** 80)') # 81/1    0.000    0.000    0.000    0.000 task1.py:52(count_odd_even_digits)


#Решение2, цикл

def count_odd_even_digits2(num):
    odd = 0
    even = 0
    while num != 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return odd, even

test_func(count_odd_even_digits2) # функция работает корректно

print(timeit.timeit('count_odd_even_digits2(6 * 10 ** 5)', globals=globals())) # 1.1859562919999007
print(timeit.timeit('count_odd_even_digits2(6 * 10 ** 10)', globals=globals())) # 2.0350667989987414
print(timeit.timeit('count_odd_even_digits2(6 * 10 ** 15)', globals=globals())) # 3.117289574998722
print(timeit.timeit('count_odd_even_digits2(6 * 10 ** 20)', globals=globals())) # 4.315496138005983
print(timeit.timeit('count_odd_even_digits2(6 * 10 ** 40)', globals=globals())) # 10.387939144995471
print(timeit.timeit('count_odd_even_digits2(6 * 10 ** 80)', globals=globals())) # 23.418212181000854

cProfile.run('count_odd_even_digits2(6 * 10 ** 5)') # 1    0.000    0.000    0.000    0.000 task1.py:81(count_odd_even_digits2)
cProfile.run('count_odd_even_digits2(6 * 10 ** 10)') # 1    0.000    0.000    0.000    0.000 task1.py:81(count_odd_even_digits2)
cProfile.run('count_odd_even_digits2(6 * 10 ** 15)') # 1    0.000    0.000    0.000    0.000 task1.py:81(count_odd_even_digits2)
cProfile.run('count_odd_even_digits2(6 * 10 ** 20)') # 1    0.000    0.000    0.000    0.000 task1.py:81(count_odd_even_digits2)
cProfile.run('count_odd_even_digits2(6 * 10 ** 40)') # 1    0.000    0.000    0.000    0.000 task1.py:81(count_odd_even_digits2)
cProfile.run('count_odd_even_digits2(6 * 10 ** 80)') # 1    0.000    0.000    0.000    0.000 task1.py:81(count_odd_even_digits2)

#Решение3, list comprehension
def count_odd_even_digits3(num):
    digits = [int(num // 10 ** i % 10) for i in range(len(str(num)))]
    odd = 0
    even = 0
    for digit in digits:
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

test_func(count_odd_even_digits3) # функция работает корректно

print(timeit.timeit('count_odd_even_digits3(6 * 10 ** 5)', globals=globals())) # 4.946049719997973
print(timeit.timeit('count_odd_even_digits3(6 * 10 ** 10)', globals=globals())) # 9.249066882002808
print(timeit.timeit('count_odd_even_digits3(6 * 10 ** 15)', globals=globals())) # 13.610342300999037
print(timeit.timeit('count_odd_even_digits3(6 * 10 ** 20)', globals=globals())) # 17.74845897900377
print(timeit.timeit('count_odd_even_digits3(6 * 10 ** 40)', globals=globals())) # 40.606429332001426
print(timeit.timeit('count_odd_even_digits3(6 * 10 ** 80)', globals=globals())) # 93.42161179299728

cProfile.run('count_odd_even_digits3(6 * 10 ** 5)') # 1    0.000    0.000    0.000    0.000 task1.py:109(count_odd_even_digits3)
cProfile.run('count_odd_even_digits3(6 * 10 ** 10)') # 1    0.000    0.000    0.000    0.000 task1.py:109(count_odd_even_digits3)
cProfile.run('count_odd_even_digits3(6 * 10 ** 15)') # 1    0.000    0.000    0.000    0.000 task1.py:109(count_odd_even_digits3)
cProfile.run('count_odd_even_digits3(6 * 10 ** 20)') # 1    0.000    0.000    0.000    0.000 task1.py:109(count_odd_even_digits3)
cProfile.run('count_odd_even_digits3(6 * 10 ** 40)') # 1    0.000    0.000    0.000    0.000 task1.py:109(count_odd_even_digits3)
cProfile.run('count_odd_even_digits3(6 * 10 ** 80)') # 1    0.000    0.000    0.000    0.000 task1.py:109(count_odd_even_digits3)

"""
Вывод:
Все три метода имеют линейную зависимость, в том числе и рекурсивный метод(чего я не ожидал).
Однако все три метода показали разное время работы. Самый худший оказался 3-ий, самый лучший 2-ой. 2-ой метод работает
примерно в 3 раза лучше, чем 1-ый, и в 4, чем 3-ий. Можно сделать вывод, что разные линейные алгоритмы могут сильно
отличаться по времени, при больших числах 3-ий алгоритм чувствительно медленние работает, чем 2-ой.
"""