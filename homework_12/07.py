N = int(input('Введите количество заказов: '))
data = dict()

for i in range(1, N + 1):
    print(i, end=' ')
    order = input('заказ: ').split(' ')
    if order[0] not in data:
        data[order[0]] = {order[1]: int(order[2])}
    else:
        if order[1] not in data[order[0]]:
            data[order[0]] |= {order[1]: int(order[2])}
        else:
            data[order[0]][order[1]] += int(order[2])

for name, pizza in sorted(data.items()):
    print(f'{name}:')
    for sort, amount in sorted(pizza.items()):
        print('    ', sort, amount)
