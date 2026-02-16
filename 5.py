row1 = input()
row2 = input()
row3 = input()
uni_row1 = set(row1)
uni_row2 = set(row2)
uni_row3 = set(row3)
unique_all = uni_row1 - uni_row2 - uni_row3 \
             | uni_row2 - uni_row1 - uni_row3 \
             | uni_row3 - uni_row2 - uni_row1
print(' '.join(unique_all))