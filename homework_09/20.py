N = int(input('Кол-во чисел: '))
list_1 = []
list_2 = []
for i in range(1, N + 1):
    k = int(input('Число: '))
    list_1.append(k)
    list_2.append(k)
for i in range(0, N - 1):
    list_1.insert(len(list_1) - i, list_2[i])
    list_3 = list(reversed(list_1))
    if list_3 == list_1:
        print(list_1)
        print('Нужно приписать чисел: ', i + 1)
        break
print('Сами числа: ', end=' ')
for i in range(len(list_1)//2 + 1, len(list_1)):
    print(list_1[i], end=' ')
