text = input('Введите текст: ')
current = 0
answer = 0
for symbol in text:
    if symbol != ' ':
        current += 1
    elif current != 0:
        answer = max(answer, current)
        current = 0
answer = max(answer, current)
print('Самое длинное слово:', answer)
