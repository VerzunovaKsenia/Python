chislo = [114, 12, 14, 10605, 4907, 450]
for i in range (0,5):
    if chislo[i] % 2 == 0 and chislo[i] % 3 != 0:
        print(chislo[i], ':число подходит')
    else:
        print(chislo[i], ':число не подходит')
