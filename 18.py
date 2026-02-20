length = int(input())
text = input()
result = ""
for i in range(len(text)):
    result += text[i]
    if (i + 1) % length == 0:
        result += "\n"
print(result)