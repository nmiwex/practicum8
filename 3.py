text = input()
founded_letters = []
for i in text:
    if i.isalpha():
        lower_letter = i.lower()
        if lower_letter not in founded_letters:
            founded_letters.append(lower_letter)
print(len(founded_letters))
