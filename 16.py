text = input()
count = 0
norm = True
for ch in text:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1
    if count < 0:
        norm = False
        break
if norm and count == 0:
    print('Скобки расставлены правильно')
else:
    print('Скобки расставлены не правильно')