formula = input()
stack = []
result = ''

# 연산자 우선순위
def p(opr):
    if opr == '+' or opr == '-':
        return 1
    elif opr == '*' or opr == '/':
        return 2
    else:
        return 0


for i in formula:
    if i.isalpha():
        result += i
        continue
    if i == '(':
        stack.append(i)
    elif i == ')':
        while(True):
            if stack and stack[-1] != '(':
                result += stack.pop()
            else:
                stack.pop()
                break
    else:
        while(True):
            if stack and (p(stack[-1]) >= p(i)):
                result += stack.pop()
            else:
                stack.append(i)
                break

while(True):
    if stack:
        result += stack.pop()
    else:
        break

print(result)