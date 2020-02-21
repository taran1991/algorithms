
#https://drive.google.com/file/d/1UVRpy328Vbe3VCG-2awfmWL1OHP7P3o9/view?usp=sharing

oper = input('Введите операцию. +,-,/,*,0-для выхода ')
if oper != '0':
    op1 = float(input('Введите число '))
    op2 = float(input('Введите число '))

while oper != '0':
    if oper != '-' and oper != '+' and oper != '/' and oper != '*':
        print('Ошибка неверный ввод операции')
    elif oper == '+':
        print(op1 + op2)
    elif oper == '-':
        print(op1 - op2)
    elif oper == '/':
        if op2 != 0:
            print(op1 / op2)
        else:
            print('На ноль делить нельзя')
    else:
        print(op1 * op2)
    oper = input('Введите операцию. +,-,/,*,0-для выхода ')
    if oper != '0':
        op1 = float(input('Введите число '))
        op2 = float(input('Введите число '))
