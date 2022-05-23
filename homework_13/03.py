size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))
file = 0
time = 1

while file < size:
    file = time * speed
    if file < size:
        print('Прошло', time, 'сек. Скачано', file, 'из', size, 'Мб (', round(file*100/size), ')%')
    else:
        print('Прошло', time, 'сек. Скачано', size, 'из', size, 'Мб (', 100, ')%')
    time += 1
