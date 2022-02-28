deposit = int(input('Сумма вклада: '))
percent = int(input('Введите количество процентов: '))
result = int(input('Вклад через несколько лет: '))
time = 0
while deposit < result:
    deposit = int(( 1 + percent / 100 ) * deposit)
    time += 1
print(time)
