#https://drive.google.com/file/d/1HGmIOBgE1UwNaZyy3pkluDDGMnalnwcE/view?usp=sharing

num = int(input('Введите натуральное трехзначное число '))

sum = num % 10
prod = num % 10
num = num // 10

sum = sum + (num % 10)
prod = prod * (num % 10)
num = num // 10

sum = sum + num
prod = prod * num

print('сумма: %s, произведение: %s' %(sum, prod))