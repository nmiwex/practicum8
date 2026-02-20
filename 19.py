text = input()
width = int(input())
words = text.split()
vowels = "аеёиоуыэюя"
current_line = []
current_len = 0
while len(words) > 0:
    word = words[0]
    if len(current_line) > 0:
        need_len = current_len + 1 + len(word)
    else:
        need_len = len(word)

    if need_len <= width:
        current_line.append(word)
        if len(current_line) == 1:
            current_len = len(word)
        else:
            current_len += 1 + len(word)
        words.pop(0)
    else:
        part1 = ""
        part2 = ""
        found_split = False
        i = 1
        while i < len(word) - 2:
            letter = word[i].lower()
            next_letter = word[i + 1].lower()
            if letter in vowels and next_letter not in vowels:
                # Пробуем разбить тут: слово[:i+1] + "-"
                temp_part1 = word[:i + 1] + "-"
                temp_part2 = word[i + 1:]
                # Проверяем, влезает ли первая часть в остаток строки
                space_needed = 0
                if len(current_line) > 0:
                    space_needed = 1
                if current_len + space_needed + len(temp_part1) <= width:
                    part1 = temp_part1
                    part2 = temp_part2
                    found_split = True
            i += 1

        if found_split == True:
            current_line.append(part1)
            words.pop(0)
            words.insert(0, part2)
        if len(current_line) == 1:
            print(current_line[0])
        else:
            total_letters = 0
            for w in current_line:
                total_letters += len(w)
            total_spaces = width - total_letters
            holes = len(current_line) - 1
            final_string = ""
            for j in range(holes):
                final_string += current_line[j]
                spaces_count = total_spaces // holes
                remainder = total_spaces % holes
                if j < remainder:
                    spaces_count += 1
                final_string += " " * spaces_count
            final_string += current_line[-1]
            print(final_string)
        current_line = []
        current_len = 0
if len(current_line) > 0:
    res = ""
    for w in current_line:
        res += w + " "
    print(res)