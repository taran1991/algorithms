
matrix = []

for i in range(5):
    arr = []
    row_sum = 0
    for j in range(3):
        num = float(input('Введите число '))
        arr.append(num)
        row_sum += num
    arr.append(row_sum)
    matrix.append(arr)

print(matrix)
