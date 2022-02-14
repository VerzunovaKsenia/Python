a = int(input('Введите число: '))
for i in range(4):
    print(a // 10**(4-i-1) % 10)
