text = input().lower()
words = text.split()
for word in words:
    if word != words[0] and len(word) == len(set(word)):
        print(word)