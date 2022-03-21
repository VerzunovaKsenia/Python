numbers = input('Введите список целых чисел: ')
l = numbers.count('0')
k = numbers.count('0')
while k != 0:
    index = numbers.find('0')
    numbers = numbers[:index] + numbers[index+1:] + '0'
    k -= 1
print(numbers[:len(numbers)-l])
