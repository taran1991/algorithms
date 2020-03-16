
"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


from collections import deque


MAPPING = {'A': 10,
           'B': 11,
           'C': 12,
           'D': 13,
           'E': 14,
           'F': 15,
           10: 'A',
           11: 'B',
           12: 'C',
           13: 'D',
           14: 'E',
           15: 'F',
           }


def _symbol_to_num(symb):
    if symb in MAPPING:
        return MAPPING[symb]
    else:
        return int(symb)

def _add_to_result(num, result):
    add = 0
    if num > 15:
        add = num // 16
        num %= 16
    if num < 10:
        result.append(str(num))
    elif 9 < num < 16:
        result.append(MAPPING[num])
    return result, add

def sum_hex_nums(first, second):
    first = first.copy()
    second = second.copy()
    first.reverse()
    second.reverse()
    len_first = len(first)
    len_second = len(second)
    if len_first > len_second:
        second.extend([0] * (len_first - len_second))
    elif len_first < len_second:
        first.extend([0] * (len_second - len_first))
    result = deque()
    add = 0
    for oper1, oper2 in zip(first, second):
        num = _symbol_to_num(oper1) + _symbol_to_num(oper2) + add
        result, add = _add_to_result(num, result)
    if add:
        result.append('1')
    result.reverse()
    return result

def multiply_hex_nums(first, second):
    first = first.copy()
    second = second.copy()
    if len(second) > len(first):
        first, second = second, first
    result = deque()
    first.reverse()
    second.reverse()
    for ind, multiplier in enumerate(second):
        add = 0
        multiplier = _symbol_to_num(multiplier)
        mul_result = deque()
        for oper in first:
            num = _symbol_to_num(oper) * multiplier + add
            mul_result, add = _add_to_result(num, mul_result)
        if add:
            if add < 9:
                mul_result.append(str(add))
            else:
                mul_result.append(MAPPING[add])
        mul_result.reverse()
        mul_result.extend([0] * ind)
        result = sum_hex_nums(result, mul_result)
    return result


first = deque(input('Введите первое число ').upper())
second = deque(input('Введите второе число ').upper())
hex_sum = sum_hex_nums(first, second)
hex_mul = 0
hex_mul = multiply_hex_nums(first, second)
print(f'сумма: {hex_sum}, произведение: {hex_mul}')



