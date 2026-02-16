cities = input().split()
winner = None
error = False
for i in range(1, len(cities)):
    prev_city = cities[i-1].lower()
    cur_city = cities[i].lower()
    if cur_city[0] != prev_city[-1]:
        error = True
        if i % 2 != 0:
            winner = 'Петя'
        else:
            winner = 'Вася'
            break
if not error:
    if len(cities) % 2 != 0:
        winner = 'Петя'
    else:
        winner = 'Вася'
print(winner, error)