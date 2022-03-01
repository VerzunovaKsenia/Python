N = int(input('Введите число карточек: '))
for i in range(2,N+2):
    k = int(input('Введите номер карточки: '))
    if i - k != 1:
        print('Потерянная карточка:', i)
        break
