income = int(input('Введите доход: '))
if(income < 10000):
    print(income*0.13)
if(10000 <= income < 50000):
    print((income - 10000)*0.2 + 1300)
if(50000 <= income):
    print((income - 50000)*0.3 + 9300)
