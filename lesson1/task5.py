print('Введите заглавные две буквы латинского алфавита. Первая буква должна идти в алфавите перед второй.')

sym1 = input('Введите первую букву ')
sym2 = input('Введите вторую букву ')

first_letter = ord('A')

num1 = ord(sym1)

num2 = ord(sym2)

place1 = num1 - first_letter + 1
place2 = num2 - first_letter + 1
syms_between = place2 - place1 - 1

print(place1, place2, syms_between)