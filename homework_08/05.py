x = 6
y = 19
while x <= 15 and y <= 20:
    print('Марсоход находится на позиции', x, y, end=' ')
    N = input('введите команду: ')
    if N == 'S':
        y -= 1
        print()
    if N == 'W':
        y += 1
    if N == 'A':
        x -= 1
    if N == 'D':
        x += 1
print('Упёрся в стену.')
