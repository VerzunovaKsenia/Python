a = int(input('Введите количество баллов по русскому языку: '))
b = int(input('Введите количество баллов по математике: '))
c = int(input('Введите количество баллов по информатике: '))
total_sum = a + b + c 
if(total_sum >= 270):
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')
