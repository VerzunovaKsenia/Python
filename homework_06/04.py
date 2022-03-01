for i in range (30,36):
    print('Людей в', i, end="")
    people = int(input('-м секторе: '))
    if people < 10:
        print('Всё спокойно.')
    else:
        print('Нарушение! Слишком много людей в секторе!')
