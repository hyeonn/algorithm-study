import sys

input = sys.stdin.readline
n = int(input().rstrip())

for i in range(n):
    s = list(input().rstrip())
    score = 0
    sum = 1
    for j in range(len(s)):
        if s[j] == 'X':
            sum = 1
        else:
            score += sum
            sum += 1
    print(score)