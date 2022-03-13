N = int(input('Количество человек: '))
K = int(input('Какое число в считалке? '))
circle = [elem for elem in range(1, N+1)]
i = 0
while(len(circle) > 1):
    i = (i + K - 1) % len(circle)
    circle.pop(i)
print(circle[0])
