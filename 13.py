ticket = input()
count = 1
happy = False
while not happy:
    fst_sum = 0
    scd_sum = 0
    for ch in range(len(ticket)):
        if ch <= len(ticket) / 2 - 1:
            fst_sum += int(ticket[ch])
        else:
            scd_sum += int(ticket[ch])
    if len(ticket) % 2 == 0 and fst_sum == scd_sum:
        happy = True
        print(count)
        break
    else:
        count += 1
        ticket = input()
'''while not happy:
    if len(ticket) % 2 == 0:
        for ch in range(len(ticket)):
            if ch <= len(ticket)/2 - 1:
                fst_sum += int(ticket[ch])
            else:
                scd_sum += int(ticket[ch])
        print(fst_sum, scd_sum)
        if fst_sum == scd_sum:
            happy = True
            print(count)
            break
    else:
        count += 1
        ticket = input()
'''