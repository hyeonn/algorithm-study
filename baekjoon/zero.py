n = int(input())
stack = []
for i in range(n):
    stack.append(int(input()))
    if stack[-1] == 0:
        stack.pop(-1)
        if len(stack)>=1:
            stack.pop(-1)
print(sum(stack))
