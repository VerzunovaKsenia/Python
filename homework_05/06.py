a = int(input('Введите число: '))
pos = 0
neg = 0
while a != 0:
    if a > 0:
        pos += 1
    if a < 0:
        neg += 1
    a = int(input('Введите число: '))
print('Количество полож чисел:' , pos)
print('Количество отриц чисел:' , neg)
