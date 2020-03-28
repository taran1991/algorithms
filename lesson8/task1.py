
# -*- coding: utf-8 -*-

"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и строку
целиком. Пример работы функции:

func("papa")
6
func("sova")
9
"""


import hashlib


def count_substrings(user_str):
    list_sub_strs = []
    for slice_ind in range(1, len(user_str)):
        for ind in range(len(user_str) - slice_ind + 1):
            slice_hash = hashlib.sha1(user_str[ind:ind + slice_ind].encode('utf-8')).hexdigest()
            if slice_hash not in list_sub_strs:
                list_sub_strs.append(slice_hash)
    return len(list_sub_strs)


print(count_substrings("papa"))
print(count_substrings("sova"))
print(count_substrings("a a "))

