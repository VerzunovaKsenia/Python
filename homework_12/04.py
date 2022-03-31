goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for elem in goods.keys():
    y = goods.get(elem)
    for key, value in store.items():
        if key == y:
            z = store.get(key)
            quantity = 0
            sum_quantity = 0
            price = 0
            for i in range(len(z)):
                quantity = z[i].get('quantity')
                sum_quantity += quantity
                price += z[i].get('price') * quantity
            print(elem, '-', quantity, 'шт, стоимость', price, 'руб')
