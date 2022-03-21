N = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
sticks = N * ['|']
for i in range(k):
    print('Бросок', i + 1, end='.')
    index_1 = int(input('Сбиты палки с номера '))
    index_2 = int(input('по номер '))
    for j in range(index_1 - 1, index_2):
        sticks[j] = '.'
print(''.join(sticks))
