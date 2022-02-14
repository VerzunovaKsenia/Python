a = int(input('Введите стоимость первого товара: '))
b = int(input('Введите стоимость второго товара: '))
c = int(input('Введите стоимость третьего товара: '))
sum_product = a + b + c
if( sum_product >= 10000):
    print(sum_product - sum_product * 0.1)
else:
    print(sum_product)
