hint = input('Введите подсказку:')
word = input('Загаданное слово:')
print('\n' * 25)
print(hint)
hidden_word = ['*'] * len(word)
print(''.join(hidden_word))
attempts_count = 0
while attempts_count < 10:
    choice = input("Буква или слово (0 - буква, 1 - слово)?")
    if choice == '0':
        letter = input()
        for ch in range(len(word)):
            if word[ch] == letter:
               hidden_word[ch] = letter
        print(''.join(hidden_word))
        if '*' not in hidden_word:
            print('Победа!')
            break
    elif choice == '1':
        entered_word = input()
        if entered_word == word:
            print('Победа!')
        else:
            print('Проигрыш :(')
        break
    attempts_count += 1
print('Проигрыш :(')