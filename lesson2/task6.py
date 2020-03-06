
import random

n = random.randint(0, 100)
guessed = False
for i in range(10):
    user_num = int(input('Введите натуральное число от 0 до 100 '))
    if user_num > n:
        print('Ваше число больше')
    elif user_num < n:
        print('Ваше число меньше')
    else:
        guessed = True
        print('Поздравляю, вы угадали!')
        break
if not guessed:
    print(n)
