N = int(input('Введите количество членов ряда: '))
series = 1
for i in range(1, N + 1):
    series += float((-1) ** N / (2 ** N))
print('Сумма ряда равна', series)
