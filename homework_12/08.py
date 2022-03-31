numbers = []

N = int(input('Введите максимальное число: '))
Boris = input('Нужное число есть среди вот этих чисел: ')
Artem = 0
for i in range(1, N + 1):
    numbers.append(i)
while Boris != 'Помогите':
    Boris = Boris.split(' ')
    Artem = input('Ответ Артёма: ')
    if Artem == 'Нет':
        for j in range(len(Boris)):
            k = Boris[j]
            if k in numbers:
                numbers.remove(k)
    if Artem == 'Да':
       numbers.clear()
       numbers = list(Boris)
    Boris = input('Нужное число есть среди вот этих чисел: ')
print('Артём мог загадать следующие числа: ',numbers)
