a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if((a >= b) and (a >= c)):
    print('Максимум:', a)
if((b > a) and (b >= c)):
    print('Максимум:', b)
if((c > a) and (c > b)):
    print('Максимум:', c)
