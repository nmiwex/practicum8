text = input()
max_spase = 0
cur_spase = 0
for i in text:
    if i == ' ':
        cur_spase += 1
        if cur_spase > max_spase:
            max_spase = cur_spase
    else:
        cur_spase = 0
print(max_spase)