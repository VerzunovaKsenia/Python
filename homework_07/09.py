x = float(input('Введите число: '))
if x % 2 == 0 and x < 65:
    print('Недопустимое значение!')
else:
    res = 1
    for i in range(1, 7):
        res *= (x - (2 ** i - 1)) / (x - 2 ** i)
    print(res)
