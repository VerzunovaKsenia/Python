N = int(input('Кол-во друзей: '))
K = int(input('Кол-во долговых расписок: '))
debt_list = []
for j in range(1, N + 1):
    debt_list.append([])
for i in range(1, K + 1):
    print(i, 'расписка:',)
    who = int(input('Кто: '))
    to = int(input('Кому: '))
    debt = int(input('Сколько: '))
    for j in range(0, N):
        if who - 1 == j:
            debt_list[j].append(-debt)
    for k in range(0, N):
        if to - 1 == k:
            debt_list[k].append(debt)
print('Баланс друзей:')
count = 1
for elem in debt_list:
    print(count, ': ', end='')
    print(sum(elem))
    count += 1
