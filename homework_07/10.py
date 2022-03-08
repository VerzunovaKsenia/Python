X = int(input('Введите количество мальчиков: '))
Y = int(input('Введите количество девочек: '))
if X > 2 * Y or Y > 2 * X:
    print('Ответ: Нет решения')
else:
    if X > Y:
        while(X <= 2*Y):
            print('BG', end='')
            Y -= 1
            X -= 1
        while(Y > 0):
            print('BBG', end='')
            Y -= 1
            X -= 2
        if (X == 1):
            print('B', end='')
    if X==Y:
        while (X != 0):
            print('BG', end='')
            X -= 1
    if Y > X:
        while (Y <= 2 * X):
            print('GB', end='')
            Y -= 1
            X -= 1
        while (X > 0):
            print('GGB', end='')
            Y -= 2
            X -= 1
        if (X == 1):
            print('G', end='')
