speed = int(input('Введите скорость: '))
time = int(input('Введите время: '))
distance = (speed * time) % 115 
print('Сумма:', distance)
