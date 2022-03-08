letters = input()
current = 0
answer = 0
for letter in letters:
    if letter == 's':
        current += 1
    elif current != 0:
        answer = max(answer, current)
        current = 0
print(answer)
