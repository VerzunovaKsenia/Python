a = int(input('Введите один конец отрезка: '))
b = int(input('Введите второй конец отрезка: '))
sum1 = 0
for i in range(a, b+1):
    sum1 += i 
print(sum1/(b-a+1))
