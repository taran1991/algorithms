
for i in range(2, 10):
    multiple_nums = 0
    for j in range(2, 100):
        if j % i == 0:
            multiple_nums += 1
    print(f'{i}: {multiple_nums}')
