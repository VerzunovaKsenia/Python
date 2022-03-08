row_number = int(input('Введите нкол-во рядов: '))
number_of_seats = int(input('Введите кол-во сидений в ряде: '))
distance = int(input('Введите кол-во метров между рядами: '))
print('Сцена')
for i in  range(1, row_number + 1):
    print(number_of_seats * '=', end=' ')
    print(distance * '*', end=' ')
    print(number_of_seats * '=')
