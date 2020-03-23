
# -*- coding: utf-8 -*-

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
 Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
творчество, фантазию и создали универсальный код для замера памяти.

Для разбора взята задача номер 2 из четвертой практической работы. Сравниваются, на пердмет потребления памяти, два
алгоритма написанных мною lesson4_task2_solve1, lesson4_task2_solve2 и алгоритм написанным преподователем
lesson4_task2_solve3.

Алгоритм в данном модуле не может работать с функциями в сторонних модулях, к сожалению. Поэтому число num в каждом
модуле меняется в ручную.
"""

import sys
import lesson4_task2_solve1
import lesson4_task2_solve2
import lesson4_task2_solve3
import os
import inspect

def obj_memmory_count(obj):
    memmory = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                memmory += obj_memmory_count(key)
                memmory += obj_memmory_count(value)
        elif not isinstance(obj, str):
            for item in obj:
                memmory += obj_memmory_count(item)
    return memmory

def module_memmory_count(module):
    memmory = 0
    for attr in dir(module):
        if not attr.startswith('__') and not inspect.ismodule(attr):
            memmory += obj_memmory_count(getattr(module, attr))
    return memmory



# num = 100 во всех трех алгоритмах
# print(module_memmory_count(lesson4_task2_solve1)) # 19876 байт
# print(module_memmory_count(lesson4_task2_solve2)) # 244 байт
# print(module_memmory_count(lesson4_task2_solve3)) # 19876 байт
#
# num = 200 во всех трех алгоритмах
# print(module_memmory_count(lesson4_task2_solve1)) # 45692 байт
# print(module_memmory_count(lesson4_task2_solve2)) # 244 байт
# print(module_memmory_count(lesson4_task2_solve3)) # 45692 байт


# # num = 400 во всех трех алгоритмах
# print(module_memmory_count(lesson4_task2_solve1)) # 103512 байт
# print(module_memmory_count(lesson4_task2_solve2)) # 244 байт
# print(module_memmory_count(lesson4_task2_solve3)) # 103512 байт

# num = 800 во всех трех алгоритмах
# print(module_memmory_count(lesson4_task2_solve1)) # 232068 байт
# print(module_memmory_count(lesson4_task2_solve2)) # 244 байт
# print(module_memmory_count(lesson4_task2_solve3)) # 232068 байт


# num = 10000 во всех трех алгоритмах
print(module_memmory_count(lesson4_task2_solve1)) # 3962520 байт
print(module_memmory_count(lesson4_task2_solve2)) # 244 байт
print(module_memmory_count(lesson4_task2_solve3)) # 3962520 байт

"""
Вывод: На моем компьютере установлена 64-битная Ubuntu и стоит 64-битный интерпритатор. Проанализировав 3 метода
решения, мы видем, что в первом и втором варианте линейное потребление памяти, чем больше у нас число num, а
следовательно и кол-во элементов в массиве, тем больше требуется памяти. Второй способ требует константное потребление
памяти (244 байта). Однако, как мы помним из задания со скоростью, второй способ является самым медленным. Если
рассматривать какой способ лучше относительно памяти, то выбор одназначно падает на второй. Но с учетом тестов на
скорость, я бы выбрал 3 реализацию алгоритма.
"""