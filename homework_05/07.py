print('Начался 8-часовой рабочий день')
hour = 1
sum_task = 0
n = 0
while hour != 9:
    print(hour, '-й час')
    task = int(input('Сколько задач решит Максим? '))
    sum_task += task
    wife = int(input('Звонит жена.Взять трубку? (1-да, 0-нет): '))
    n += wife
    hour += 1
print('Рабочий день закончился.Всего выполнено задач:', sum_task)
if n != 0:
    print('Нужно зайти в магазин.')
