letters = input('Введите строку: ')
for index, letter in enumerate(letters):
    if letter == 'a':
        print(0, end=' ')
    if letter == 'b':
        print((index + 1) * 2, end=' ')
