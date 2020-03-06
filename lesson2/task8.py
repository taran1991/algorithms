
def count_digit_in_num(digit, num):
    quantity = 0
    while num != 0:
        if digit == num % 10:
            quantity += 1
        num = num // 10
    return quantity


digit = int(input('Введите цифру '))
nums_quan = int(input('Введите кол-во чисел ввода '))
quantity = 0
for i in range(nums_quan):
    n = int(input('Введите число '))
    quantity += count_digit_in_num(digit, n)
print(quantity)

