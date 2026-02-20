def number_to_text(n):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть",
            "семь", "восемь", "девять"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать",
             "четырнадцать", "пятнадцать", "шестнадцать",
             "семнадцать", "восемнадцать", "девятнадцать"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    units_fem = ["", "одна", "две", "три", "четыре", "пять", "шесть",
                 "семь", "восемь", "девять"]

    def convert_number(number, gender=0):
        parts = []
        h = number // 100
        if h > 0:
            parts.append(hundreds[h])
        t = number % 100
        if t == 0:
            pass
        elif t < 10:
            if gender == 1:
                parts.append(units_fem[t])
            else:
                parts.append(units[t])
        elif t < 20:
            parts.append(teens[t - 10])
        else:
            decade = t // 10
            unit = t % 10
            parts.append(tens[decade])
            if unit > 0:
                if gender == 1:
                    parts.append(units_fem[unit])
                else:
                    parts.append(units[unit])

        return " ".join(parts)


    def get_ending(number, form1, form2, form5):
        num = number % 100
        if 11 <= num <= 19:
            return form5
        num = num % 10
        if num == 1:
            return form1
        if 2 <= num <= 4:
            return form2
        return form5


    result = []
    millions = n // 1_000_000
    if millions != 0:
        text = convert_number(millions, 0)
        ending = get_ending(millions, "миллион", "миллиона", "миллионов")
        result.append(f"{text} {ending}")
    thousands = (n % 1_000_000) // 1000
    if thousands != 0:
        text = convert_number(thousands, 1)
        ending = get_ending(thousands, "тысяча", "тысячи", "тысяч")
        result.append(f"{text} {ending}")
    ones = n % 1000
    if ones != 0:
        text = convert_number(ones, 0)
        result.append(text)
    return " ".join(result)


users_number = int(input())
print(number_to_text(users_number))