text = input()
words = text.split()
sorted_words = sorted(words, key=len)
print(' '.join(sorted_words))