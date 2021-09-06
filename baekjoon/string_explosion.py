# 여러줄이 입력될 때 - sys의 sys.stdin.readline              !사용법 찾아보기!
# rstrip() 오른쪽 개행문자 삭제, strip() 모든 개행문자 삭제
# .join(리스트명) <- 리스트를 스트링으로 합쳐줌

import sys

input = sys.stdin.readline
s = list(input().rstrip())
bomb = list(input().rstrip())
l = len(bomb)

stack = []

for i in s:
    stack.append(i)
    if bomb[-1] == stack[-1] and len(stack) >= l:
        if bomb == stack[-l:]:
            for j in range(l):
                stack.pop()
if stack:
    print("FRULA")
else:
    print("".join(stack))