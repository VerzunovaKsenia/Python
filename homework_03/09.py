distance = int(input('Введите пробег: '))
date = int(input('Введите сегодняшнее число: '))
a = distance % 10 
b = distance // 10 % 10
c = distance // 100
if(a + b + c > date):
    print('Сброс.')
    print('Пробег: 0')
else:
    print('Сегодня не сломался.')
    print('Пробег:', distance)
