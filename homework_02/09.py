a = int(input('Введите число: '))
b = 0
for i in range(4):
    b = b * 10 + (a // 10**(i) % 10) * 10
print(b//10)
