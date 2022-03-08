message = input('Введите зашифрованное сообщение: ')
length = len(message)
word = ['']*length
j = 0
for i in range(length):
    if i % 2 == 0:
        word[j] = message[i]
    else:
        word[length-j-1] = message[i]
        j += 1
print(''.join(word))