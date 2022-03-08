a = float(input('Введите ширину письма: '))
a_max = a
a_min = a
n = 0
while a_max > 12:
    a_max /= 2
    a_max, a_min = max(a_max, a_min), min(a_max, a_min)
    n += 1
print('Письмо нужно свернуть', n, 'разa.')
