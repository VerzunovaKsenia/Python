letters = input('Введите строку: ')
index_1 = letters.find('h')
index_2 = letters.find('h', index_1 + 1)
print(letters[index_2 - 1:index_1:-1])
