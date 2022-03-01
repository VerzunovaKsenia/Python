N = int(input('Введите количество учеников: '))
three = 0
four = 0
five = 0
for i in range(1, N+1):
    grade = int(input('Введите оценку: '))
    if grade == 3:
        three += 1
    if grade == 4:
        four += 1
    if grade == 5:
        five += 1
if three == max(three,four,five):
    print('Больше троечников.')
if four == max(three,four,five):
    print('Больше хорошистов.')
if five == max(three,four,five):
    print('Больше отличников.')
