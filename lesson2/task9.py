
def count_digits_sum(num):
    dig_sum = 0
    while num != 0:
        dig_sum += num % 10
        num = num // 10
    return dig_sum


nums_quan = int(input('Введите кол-во чисел ввода '))
max_sum = 0
max_num= 0
for i in range(nums_quan):
    n = int(input('Введите число '))
    dig_sum = count_digits_sum(n)
    if dig_sum > max_sum:
        max_sum = dig_sum
        max_num = n
print(f'наибольшая сумма цифр в числе {max_num} - {max_sum}')

