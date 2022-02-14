hours = int(input('Количество отработанных часов: '))
remainder = int(input('Остаток по кредиту: '))
money_for_food = int(input('Количество денег на еду: '))
salary = (200 * hours / 8) + hours
if(salary >= remainder + money_for_food):
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')
