time = int(input('Сколько минут до взрыва? '))
for i in range(time, -1, -1):
    answer = input('Хотите обезвредить бомбу? ')
    if answer == 'да':
        print('Бомба обезврежена за', time - i, 'мин.')
        break
else:
    print('Бомба взорвалась.')
