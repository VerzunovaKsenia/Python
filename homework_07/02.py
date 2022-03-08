N = int(input('Введите количество должников: '))
sum1 = 0
for i in range(0, N, 5):
    print('Должник с номером', i)
    credit = int(input('Введите сумму вашего долга: '))
    sum1 += credit
print('Общая сумма долга:', sum1)
