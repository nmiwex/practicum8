text = input()
words = text.split()
min_len = len(min(words, key=len))
print(min_len)