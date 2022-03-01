salary = int(input('Зарплата в этом месяце: '))
k = 0
for i in range(1,10):
    salary_next = int(input('Зарплата в этом месяце: '))
    if salary_next < salary:
        print('Неупорядочено')
        break
    else:
        k += 1
if k == 9:
    print('Упорядочено')
