N = int(input('Введите длину списка: '))
numbers = []
for i in range(N):
    if i % 2 == 0:
        numbers.append(1)
    else:
        numbers.append(i % 5)
print(numbers)
