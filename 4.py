text = input()
required = None
for ch in text:
    if text.count(ch) == 3:
        required = ch
print(required)