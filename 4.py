text = input()
repeat = None
for ch in text:
    if text.count(ch) == 3:
        repeat = ch
print(repeat)