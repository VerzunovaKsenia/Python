N = int(input('Загадайте число от 1 до 100: '))
a = 1
b = 100
answer = 0
k = 1
while answer != 1:
    number = int((a + b)/2)
    print('Ваше число равно(1), больше(2) или меньше(3) числа', number, '?')
    answer = int(input())
    if answer == 2:
        a = number + 1
    elif answer == 3:
        b = number - 1
    k += 1
print('Вы загадали число:', number)
print('Количество попыток:', k)
