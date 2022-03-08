text = input('Введите текст: ')
for i in range(len(text)):
    if text[i] == '*':
        print('Символ ‘*’ стоит на позиции', i + 1)
