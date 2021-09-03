n = int(input())
stack = []

for i in range(n):
    stack.append(int(input()))
    # 0일 때 스택에서 제거
    if stack[-1] == 0:
        stack.pop(-1)
        # 0 이전 숫자 삭제
        if len(stack)>=1:
            stack.pop(-1)

print(sum(stack))