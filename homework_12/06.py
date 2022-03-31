alph_1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
synonims = dict()

N = int(input('Введите количество пар слов: '))
for i in range(1, N + 1):
    print(i, end=' ')
    text = input('пара: ').lower().split(' - ')
    print(text[0])
    synonims[text[0]] = text[1]
    synonims[text[1]] = text[0]

while True:
    word = input('Введите слово: ').lower()
    if word in synonims:
        print('Синоним:', synonims[word])
    else:
        print('Такого слова в словаре нет.')
