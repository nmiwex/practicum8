text = input()
expression = []
num = ''
for ch in text:
    if ch in '()+/*-':
        if num != '':
            expression.append(num)
            num = ''
        expression.append(ch)
    elif ch in '0123456789':
        num += ch
if num != '':
    expression.append(num)

def mul_div(expr):
    i = 0
    while i < len(expr):
        if expr[i] == '*':
            result = float(expr[i-1]) * float(expr[i+1])
            expr[i-1:i+2] = [result]
        elif expr[i] == '/':
            result = float(expr[i-1]) / float(expr[i+1])
            expr[i-1:i+2] = [result]
        else:
            i += 1
    return expr


def sum_dif(expr):
    i = 0
    while i < len(expr):
        if expr[i] == '+':
            result = float(expr[i-1]) + float(expr[i+1])
            expr[i-1:i+2] = [result]
        elif expr[i] == '-':
            result = float(expr[i-1]) - float(expr[i+1])
            expr[i-1:i+2] = [result]
        else:
            i += 1
    return expr


def evaluation(expr):
    while '(' in expr or ')' in expr:
        open_bracket, close_bracket = 0, 0
        for ch in range(len(expr)):
            if expr[ch] == '(':
                open_bracket = ch
            elif expr[ch] == ')':
                close_bracket = ch
                break
        expr[open_bracket:close_bracket + 1] = evaluation(expr[open_bracket + 1:close_bracket])
    if '*' in expression or '/' in expression:
        mul_div(expression)
    elif '+' in expression or '-' in expression:
        sum_dif(expression)
    return expr


while len(expression) != 1:
    expression = evaluation(expression)
print(*expression)
#jdjkdshgjkk (4783-3838+(8348*487)) djndjjnd