violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
N = int(input('Сколько песен выбрать?: '))
sumtime = 0
#print([elem for elem in (violator_songs)])
for i in range(N):
    print('Название', i + 1, end=' ')
    song = input('песни: ')
    for j in (violator_songs):
        if j[0] == song:
            sumtime += j[1]
print('Общее время звучания песен: %.2f' % sumtime, 'минут')
