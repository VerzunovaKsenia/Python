name = input('??????? ???? ???: ')
credit = int(input('??????? ????? ?????: '))
fee = int(input('??????? ?????? ?? ???????? '))
while(credit > fee):
    print('????????,', name, '. ??????? ??? ???.')
    fee = int(input('??????? ?????? ?? ???????? '))
print('???????,', name, '! ?? ???????? ????. ???????!')
