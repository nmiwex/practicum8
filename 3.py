text = input()
founded_letters = []
for ch in text:
    if ch.isalpha() and ch.lower() not in founded_letters:
        founded_letters.append(ch.lower())
print(len(founded_letters))
