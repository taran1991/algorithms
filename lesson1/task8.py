
year = int(input('Введите год '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Год высокосный')
        else:
            print('Год не высокосный')
    else:
        print('Год высокосный')
else:
    print('Год не высокосный')