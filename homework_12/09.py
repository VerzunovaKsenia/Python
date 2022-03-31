tree = dict()
N = int(input('Введите количество человек: '))
for i in range(1, N):
    print(i, end=' ')
    child, parent = input('пара: ').split(' ')
    tree[child] = parent

result = dict()
for name_1 in tree.values():
    if name_1 not in tree.keys():
        result[name_1] = 0
for name_2 in tree.keys():
    result[name_2] = result[tree[name_2]] + 1

print('Высота каждого члена семьи: ')
for key in result:
    print(key, result[key])
