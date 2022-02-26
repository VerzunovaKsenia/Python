price = int(input('Введите стоимость квартиры: '))
area = int(input('Введите площадь квартиры: '))
if((area >= 100 and price <= 10000000) or (area >= 80 and price <= 7000000)):
    print('Подходит!')
else:
    print('Не подходит')
