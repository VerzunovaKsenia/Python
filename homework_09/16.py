list_1 = []
list_2 = []
for i in range(3):
    N = int(input('Введите число для первого списка:'))
    list_1.append(N)
for i in range(7):
    N = int(input('Введите число для второго списка:'))
    list_2.append(N)
print(list(set(list_1 + list_2)))
