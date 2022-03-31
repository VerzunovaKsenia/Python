text = input('Введите текст: ')
symbols = dict()

for i in range(len(text)):
    if text[i] not in symbols:
        symbols[text[i]] = 1
    else:
        symbols[text[i]] += 1

print(symbols)
