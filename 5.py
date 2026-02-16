x = input()
y = input()
z = input()
uni_x = set(x)
uni_y = set(y)
uni_z = set(z)
unique_all = uni_x - uni_y - uni_z | uni_y - uni_x - uni_z | uni_z - uni_y - uni_x
print(' '.join(unique_all))