dayx = input('Введите день недели: ')
n = 0
for day in ('понедельник','вторник','среда','четверг','пятница','суббота','воскресенье'):
    n += 1
    if day == dayx:
        print('Номер дня недели:', n)
