import string

x1 = int(input('Введите x координатy первой точки '))
y1 = int(input('Введите y координатy первой точки '))

x2 = int(input('Введите x координатy второй точки '))
y2 = int(input('Введите y координатy второй точки '))

if x1 == x2:
    print('x=%s' % x1)
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print('y=%s*x+%s' % (k, b))