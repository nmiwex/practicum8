text = input().lower()
words = text.split()
founded_words = []
repeat = None
for word in words:
    if word in founded_words:
        repeat = word
    else:
        founded_words.append(word)
print(repeat)