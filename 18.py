width = int(input())
text = input()
result = ""
for i in range(len(text)):
    result += text[i]
    if (i + 1) % width == 0:
        result += "\n"
print(result)