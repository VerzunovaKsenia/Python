grant = float(input('Введите сумму ежемесячной стипендии: '))
expenses = float(input('Введите сумму ежемесячных расходов: '))
sum1 = 0
for month in range(1, 11):
    sum1 += expenses - grant
    expenses = expenses * 1.03
print('Нужно получить у родителей', sum1)
