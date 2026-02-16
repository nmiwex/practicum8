text = input()
cur_count = 0
max_count = 0
prev = None
for ch in text:
    if ch == prev:
        cur_count += 1
    else:
        prev = ch
        cur_count = 1
    if cur_count > max_count:
        max_count = cur_count
print(max_count)