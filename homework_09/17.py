n = int(input('Кол-во коньков: '))
size_list = []
for i in range(1, n + 1):
    print('Размер', i, 'пары: ', end='')
    size = int(input())
    size_list.append(size)
m = int(input('Кол-во людей: '))
people_list = []
for j in range(1, m + 1):
    print('Размер ноги', j, 'человека: ', end='')
    N = int(input())
    people_list.append(N)
size_list.sort(reverse=True)
people_list.sort(reverse=True)
i = 0
j = 0
count = 0
while i != n and j != m:
    if size_list[i] >= people_list[j]:
        i += 1
        j += 1
        count += 1
    else:
        j += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
