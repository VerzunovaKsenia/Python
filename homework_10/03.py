import random

participants_1 = []
participants_2 = []
winners = []
for i in range(20):
    participants_1.append(int(random.uniform(5, 10)*100) / 100)
    participants_2.append(int(random.uniform(5, 10)*100) / 100)
    winners.append(max(participants_1[i], participants_2[i]))
print('Первая команда:', participants_1)
print('Вторая команда:', participants_2)
print('Победители тура:', winners)
