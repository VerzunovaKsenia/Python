a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if((a == b) and (a == c)):
    print("3 числа совпадают")
if(((a == b) or (a == c)) and (b != c) or ((b == c) or (b == a)) and (a != c) or ((c == b) or (c == a)) and (a != b)):
    print("2 числа совпадают")
if((a != b) and (b != c) and (a != c)):
    print("0 чисел совпадают")
