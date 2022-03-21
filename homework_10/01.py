vowels = {'а' : 1, 'о' : 1, 'у' : 1, 'е' : 1, 'ё' : 1, 'ю' : 1, 'ы' : 1, 'и' : 1, 'э' : 1, 'я' : 1}
text = input('Введите текст: ')
vowel_text = []
for i in text:
    if vowels.get(i):
        vowel_text.append(i)
print('Список гласных букв', vowel_text)
print('Длина списка:', len(vowel_text))
