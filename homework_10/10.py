alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
message = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
encrypter = {}
for i, elem in enumerate(alphabet):
    encrypter[elem] = alphabet[(i+k) % len(alphabet)]
encrypted_message = ''
for i in message:
    if encrypter.get(i):
        encrypted_message += encrypter[i]
    else:
        encrypted_message += i
print('Зашифрованное сообщение:', encrypted_message)
