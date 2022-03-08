a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
c = int(input('Введите делитель: '))
count = 0
average = 0
for n in range(a,b + 1):
    if n % c == 0:
        count += 1
        average += n
average = float(average / count)
print('Среднее арифметическое чисел на отрезке от', a, 'до', b,',делящихся на', c,'равно', average)
