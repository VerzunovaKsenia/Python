text = input('Введите строку: ')
letters = dict()
even = 0
odd = 0

for i in range(len(text)):
    if text[i] in letters:
        letters[text[i]] += 1
    if text[i] not in letters:
        letters[text[i]] = 1

if len(text) % 2 != 0:
    for value in letters.values():
        if value % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 1:
        print('Можно сделать палиндром.')
    else:
        print('Нельзя сделать палиндром.')

if len(text) % 2 == 0:
    for value in letters.values():
        if value % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        print('Можно сделать палиндром.')
    else:
        print('Нельзя сделать палиндром.')

