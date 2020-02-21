num = int(input('Введите номер место буквы латинского алфавита '))

first_letter = ord('A')
num_letter = first_letter + num - 1
sym = chr(num_letter)

print(sym)