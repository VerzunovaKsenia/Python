experience = int(input('Введите количество опыта: '))
if(experience < 1000):
    print('Ваш уровень: 1')
if(1000 <= experience < 2500):
    print('Ваш уровень: 2')
if(2500 <= experience < 5000):
    print('Ваш уровень: 3')
if(5000 <= experience):
    print('Ваш уровень: 4')
