alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
encrypter = {}
for i, elem in enumerate(alphabet):
    encrypter[elem] = alphabet[(i - k) % len(alphabet)]
encrypted_message = ''
for i in message:
    if encrypter.get(i):
        encrypted_message += encrypter[i]
    else:
        encrypted_message += i
print('Зашифрованное сообщение:', encrypted_message)
