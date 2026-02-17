hidden_num = input('Загаданное число:')
if len(hidden_num) != 4 and len(hidden_num) != len(set(hidden_num)):
    hidden_num = input('Введите другое число:')
print('\n' * 25)
attempts_count = 0
while attempts_count < 10:
    cow = 0
    bull = 0
    entered_num = input()
    for ch in range(len(hidden_num)):
        if entered_num[ch] in hidden_num:
            cow += 1
            if ch == hidden_num.index(entered_num[ch]):
                bull += 1
    print(f'Быков: {bull} Коров: {cow}')
    if entered_num == hidden_num:
        print('Победа!')
    attempts_count += 1
print('Проигрыш :(')