k = 0
for i in range (0,10):
    number = int(input('Введите число: '))
    if number % 2 == 0 and number > 0:
        k += 1
print(k)
