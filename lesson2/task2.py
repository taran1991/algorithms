
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


num = int(input('Введите натуральное число '))
odd, even = count_odd_even_digits(num)
print(f'{even} четных цифр, {odd} нечетных цифр')