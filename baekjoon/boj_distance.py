MAX = 9999999

def prev(x):
    if x == 'B':
        return 'J'
    elif x == 'O':
        return 'B'
    elif x == 'J':
        return 'O'

# dp문제: bottom-up으로 문제 해결해야함

n = int(input())
street = list(input())
dp = [MAX]*(n+1)     # 몇 칸 건너뛸지에 대한 배열
dp[0] = 0

for i in range(1, n):
    p = prev(street[i])
    for j in range(i):       # 0부터 i-1까지
        if street[j] == p:   # prev가 j번째와 같으면 dp에 저장하기
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

print(dp[n - 1] if dp[n - 1] != MAX else -1)